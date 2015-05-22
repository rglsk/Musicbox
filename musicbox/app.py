import os
from werkzeug import secure_filename

from flask import Flask
from flask import render_template
from flask import request, redirect
from flask import session
from flask.ext.socketio import SocketIO
from flask.ext.socketio import emit

import settings
import utils


app = Flask(__name__)
app.config.from_object(os.environ.get('MUSICBOX_CONFIG_MODULE',
                                      'musicbox.settings'))
socketio = SocketIO(app)


@app.route('/stream')
def index():
    return render_template('index.html')


@socketio.on('my broadcast event', namespace='/test')
def broadcast_file_info(message):
    session['receive_count'] = session.get('receive_count', 0) + 1
    emit('my response',
         {'data': message['data'], 'count': session['receive_count']},
         broadcast=True)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        _file = request.files['file']
        if _file and utils.allowed_file(_file.filename):
            filename = secure_filename(_file.filename)
            _file.save(os.path.join(settings.UPLOAD_FOLDER, filename))
    return redirect('/stream')

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
