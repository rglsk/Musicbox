import xmltodict
from xml.parsers.expat import ExpatError

from musicbox import settings
from musicbox import errors


def parse_current_song():
    """Parse XML which contain current played song on stream.

    Returns title of song. Otherwise, this method should raise NotPlayedSong.

    * NOTE:: generating json in deefuzzer is not working correctly (that's why
             xml parse)
    """
    xml = open(''.join([settings.MUSIC_FOLDER,
                        settings.CURRENT_MUSIC_PLAYED])).read()
    try:
        parsed_xml = xmltodict.parse(xml)
        return parsed_xml['rss']['channel']['item']['title']
    except KeyError:
        raise errors.IncorrectXmlError('Radio is not playing now.')
    except ExpatError:
        raise errors.IncorrectXmlError(
            '{} file is incorrect'.format(settings.CURRENT_MUSIC_PLAYED))
