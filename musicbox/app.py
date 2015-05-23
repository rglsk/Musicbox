import os
from werkzeug import secure_filename
from gevent import monkey
monkey.patch_all()  # nopep8
import time
from threading import Thread

from flask import Flask
from flask import redirect
from flask import render_template
from flask import request
from flask.ext.socketio import SocketIO
from flask.ext.socketio import emit

from musicbox import errors
from musicbox import settings
from musicbox import utils
from musicbox.db import db
from musicbox.stream import parse_current_song


app = Flask(__name__)
app.config.from_object(os.environ.get('MUSICBOX_CONFIG_MODULE',
                                      'musicbox.settings'))
socketio = SocketIO(app)
thread = None
_db = db.SongStorage()


def background_thread():
    """Backgroud thread to emit current song and playlist"""
    title = ''
    while True:
        try:
            title = parse_current_song()
        except errors.IncorrectXmlError:
            # This occurs when stream change song and xml is not parsable
            title = ''
        song_list = _db.get_all_titles()
        time.sleep(2)
        socketio.emit('current song response',
                      {'current_song': title, 'song_list': song_list},
                      namespace='/test')


@app.route('/')
def index():
    """Main view which run worker (thread) and render template."""
    global thread
    if thread is None:
        thread = Thread(target=background_thread)
        thread.start()
    return render_template('index.html')


@socketio.on('my broadcast event', namespace='/test')
def broadcast_file_info(message):
    """Broadcast socketio emits uploaded file information.

    :param message: Information message. (Dictionary)
    """
    response_data = {'data': message['data']}
    emit('my response', response_data, broadcast=True)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    """Upload audio files.

    *NOTE:: Upload files only with extension specified in ALLOWED_EXTENSIONS.
    """
    if request.method == 'POST':
        _file = request.files['file']
        if _file and utils.allowed_file(_file.filename):
            filename = secure_filename(_file.filename)
            _file.save(os.path.join(settings.UPLOAD_FOLDER, filename))
            _db.create(title=filename)
    return redirect('/')


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
