import unittest
from collective.easyslideshow.tests.base import TestCase


class TestSlideView(TestCase):

    def test_getimages(self):
        self.fail()


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSlideView))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
