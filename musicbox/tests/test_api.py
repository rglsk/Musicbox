from musicbox import settings
from musicbox.testing import BaseApiTest


class TestViews(BaseApiTest):

    def setUp(self):
        super(TestViews, self).setUp()

    def test_items_handler_live(self):
        result = self.get('/stream')
        self.assertEqual(result.status_code, 200)
        self.assertIn(settings.STREAM_URL, result.data)
