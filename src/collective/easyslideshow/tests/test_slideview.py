import unittest
from collective.easyslideshow.tests.base import TestCase
from collective.easyslideshow.browser.slideshowview import SlideshowView


class TestSlideView(TestCase):

    def afterSetUp(self):
        """This method is called before each single test. It can be used to
        set up common state. Setup that is specific to a particular test
        should be done in that test method.
        """
        self.slideshow_view = SlideshowView(self.portal, None)
        self.image_ids = ['image1', 'image2']
        #Create sample content to ensure view methods' catalog queries are
        #correct
        self.slideshow = self._createType(self.portal, 'Folder', 'slideshow')
        for img_id in self.image_ids:
            self._createType(self.slideshow, 'Image', img_id)
        self._createType(self.slideshow, 'Document', 'page1')

    def _test_img_order(self, method, ids):
        i = 0
        for obj in method('slideshow'):
            #Ensure only images get returned
            self.assertEqual(obj.portal_type, 'Image')
            #Ensure the order is the expected one
            self.assertEqual(obj.getId, ids[i])
            i += 1
        #Ensure we have the right number of images
        self.assertEqual(i, len(ids))

    def test_getImages(self):
        #Ensure image order is the original creation order
        self._test_img_order(self.slideshow_view.getImages,
                             self.image_ids)

        reversed_ids = list(reversed(self.image_ids))
        i = 0
        #Move items around
        for img_id in reversed_ids:
            obj = self.slideshow[img_id]
            self.slideshow.moveObjectToPosition(img_id, i)
            obj._p_changed = 1
            obj.reindexObject()
            i += 1

        #Ensure order is reversed
        self._test_img_order(self.slideshow_view.getImages,
                             reversed_ids)

    def test_getPortletImages(self):
        self.fail()


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSlideView))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
