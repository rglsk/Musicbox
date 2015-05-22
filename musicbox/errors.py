import logging


class BaseException(Exception):
    """ Base exception class. """

    def __init__(self, message=None):
        self.message = message
        logging.error('%s: %s', self.__class__.__name__, self.message)
        super(BaseException, self).__init__(self.message)


class NotPlayedSong(BaseException):
    """Exception error class for non-played song"""
