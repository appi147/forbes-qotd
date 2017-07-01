from forbesqotd import qotd
import unittest


class QotdTest(unittest.TestCase):

    def test_qotd(self):
        app = qotd.forbes()
        s = app.get_quote()
        self.assertTrue(isinstance(s, basestring))


if __name__ == '__main__':
    unittest.main()
