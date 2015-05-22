import os
from werkzeug import secure_filename
from gevent import monkey
monkey.patch_all()
import time

from threading import Thread
from flask import Flask
from flask import render_template
from flask import request, Response
from flask import session
from flask.ext.socketio import SocketIO
from flask.ext.socketio import emit

from musicbox import settings
from musicbox import utils
from musicbox.stream import parse_current_song


app = Flask(__name__)
app.config.from_object(os.environ.get('MUSICBOX_CONFIG_MODULE',
                                      'musicbox.settings'))
socketio = SocketIO(app)
thread = None


def background_thread():
    song_title = ''
    while True:
        parsed_xml = parse_current_song()
        if song_title == parsed_xml:
            continue
        song_title = parsed_xml
        socketio.emit('current song response', {'current_song': song_title},
                      namespace='/test')
        time.sleep(4)


@app.route('/')
def index():
    global thread
    if thread is None:
        thread = Thread(target=background_thread)
        thread.start()
    return render_template('index.html')


@socketio.on('my broadcast event', namespace='/test')
def broadcast_file_info(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    response_data = {'data': message['data'],
                     'count': session['receive_count']}
    emit('my response', response_data, broadcast=True)


# @socketio.on('broadcast current song', namespace='/test')
# def broadcast_current_song(message):
#     song_title = ''
    # while True:
    #     if song_title == parse_current_song():
    #         continue
    #     song_title = parse_current_song()
    #     emit('current song response', {'current_song': song_title})
    #     gevent.sleep(2)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        _file = request.files['file']
        if _file and utils.allowed_file(_file.filename):
            filename = secure_filename(_file.filename)
            _file.save(os.path.join(settings.UPLOAD_FOLDER, filename))
    return Response()


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
