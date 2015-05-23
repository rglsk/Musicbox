import datetime

from pymongo import MongoClient
from pymongo import ASCENDING

from musicbox.settings import SONG_CHAR_LIMIT
from musicbox.utils import to_timestamp


class SongStorage(object):
    """Manages songs and connects to Mongo database."""
    db_name = 'musicbox_db'
    collecton_name = 'songs'

    def __init__(self, host='localhost', port=27017):
        _client = MongoClient(host, port)
        self.db = _client[self.db_name]

    def create(self, title=None):
        """Creates song object.
        :param title: Title of song (String)

        Returns id of song object from mongo (String).
        """
        if title:
            timestamp = to_timestamp(datetime.datetime.now())
            return self.db[self.collecton_name].insert_one(
                {'timestamp': timestamp,
                 'title': title}).inserted_id
        return None

    def get_all(self, limit, direction=ASCENDING):
        return self.db[self.collecton_name].find().limit(limit).sort(
            'timestamp', direction)

    def get_all_titles(self, limit=6):
        all_songs = self.get_all(limit)
        return [song['title'][:SONG_CHAR_LIMIT] for song in all_songs]
