import time

import settings


def allowed_file(filename):
    return any([filename.endswith(ext) for ext in settings.ALLOWED_EXTENSIONS])


def to_timestamp(date_time):
    return time.mktime(date_time.timetuple())
