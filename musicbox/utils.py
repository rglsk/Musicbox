import settings


def allowed_file(filename):
    return any([filename.endswith(ext) for ext in settings.ALLOWED_EXTENSIONS])
