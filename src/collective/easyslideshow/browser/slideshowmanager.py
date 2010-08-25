from zope.annotation.interfaces import IAnnotations
from persistent.dict import PersistentDict

SLIDESHOW_MANAGER_PROPERTIES = 'easyslideshow.slideshowmanager.props'

class SlideshowManagerAdapter(object):
    """
    """

    def __init__(self, context):
        self.context = context
        self.annotations = IAnnotations(self.context)
        if self.annotations.get(SLIDESHOW_MANAGER_PROPERTIES, None) is None:
            self.annotations[SLIDESHOW_MANAGER_PROPERTIES] = PersistentDict()

    def getSlideshowProperties(self):
        return self.annotations[SLIDESHOW_MANAGER_PROPERTIES]

    def setSlideshowProperty(self, key, data):
        self.annotations[SLIDESHOW_MANAGER_PROPERTIES][key] = data

    def resetSlideshowProperty(self, key):
        self.annotations[SLIDESHOW_MANAGER_PROPERTIES].pop(key)

