try:
    from musicbox.local_settings import *
except Exception:
    raise('Create local_settings.py with basic configs.')


DEBUG = True
UPLOAD_FOLDER = '/home/vagrant/musicbox/musicbox/static/music/one'
STATIC_FOLTER = '/home/vagrant/musicbox/musicbox/static/music/'
ALLOWED_EXTENSIONS = set(['mp3'])
SECRET_KEY = 'secret!'
CURRENT_MUSIC_PLAYED = 'stream_mp3_current.xml'

STREAM_URL = DEBUG and '127.0.0.1:8000/stream' or 'production/url/'
