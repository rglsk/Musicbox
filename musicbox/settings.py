try:
    from musicbox.local_settings import *
except Exception:
    raise('Create local_settings.py with basic configs.')


DEBUG = True
UPLOAD_FOLDER = '/home/vagrant/musicbox/musicbox/static/music'
ALLOWED_EXTENSIONS = set(['mp3'])
SECRET_KEY = 'secret!'
