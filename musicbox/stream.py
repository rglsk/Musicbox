import xmltodict

from musicbox import settings
from musicbox import errors


def parse_current_song():
    xml = open(''.join([settings.UPLOAD_FOLDER,
                        settings.CURRENT_MUSIC_PLAYED])).read()
    parsed_xml = xmltodict.parse(xml)
    try:
        return parsed_xml['rss']['channel']['item']['title']
    except KeyError:
        raise errors.NotPlayedSong('Radio is no playing now.')
