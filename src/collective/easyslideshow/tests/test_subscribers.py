import unittest
from collective.easyslideshow.tests.base import TestCase


class TestSubscribers(TestCase):

    def test_slidesync(self):
        self.fail()


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSubscribers))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
