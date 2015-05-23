import unittest

import mock

from musicbox import errors
from musicbox.stream import parse_current_song


class TestStream(unittest.TestCase):

    @mock.patch('__builtin__.open')
    def test_parse_current_song(self, mock_open):
        title = 'ptaki.lataja.kluczem.mp3'
        example_xml = """<rss version="2.0"><channel><item><title>{}</title>
                         </item></channel></rss>""".format(title)

        mock_read = mock.Mock()
        mock_read.read.return_value = example_xml
        mock_open.return_value = mock_read

        response = parse_current_song()
        self.assertEqual(response, title)

    @mock.patch('__builtin__.open')
    def test_parse_current_song_key_error(self, mock_open):
        title = 'ptaki.lataja.kluczem.mp3'
        incorrect_example_xml = '<title>{}</title>'.format(title)

        mock_read = mock.Mock()
        mock_read.read.return_value = incorrect_example_xml
        mock_open.return_value = mock_read

        with self.assertRaises(errors.IncorrectXmlError):
            parse_current_song()

    @mock.patch('__builtin__.open')
    def test_parse_current_song_parse_error(self, mock_open):
        title = 'ptaki.lataja.kluczem.mp3'
        incorrect_example_xml = ''.format(title)

        mock_read = mock.Mock()
        mock_read.read.return_value = incorrect_example_xml
        mock_open.return_value = mock_read

        with self.assertRaises(errors.IncorrectXmlError):
            parse_current_song()
