import xmltodict

from musicbox import settings
from musicbox import errors


def parse_current_song():
    """Parse XML which contain current played song on stream.

    Returns title of song. Otherwise, this method should raise NotPlayedSong.

    * NOTE:: generating json in deefuzzer is not working correctly (that's why
             xml parse)
    """
    xml = open(''.join([settings.STATIC_FOLTER,
                        settings.CURRENT_MUSIC_PLAYED])).read()
    parsed_xml = xmltodict.parse(xml)
    try:
        return parsed_xml['rss']['channel']['item']['title']
    except KeyError:
        raise errors.NotPlayedSong('Radio is no playing now.')
