from zope.interface import implements

from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName

from Acquisition import aq_inner

from collective.easyslideshow.browser.interfaces import IEasySlideshowView

class SlideshowView(BrowserView):
    """View class for the Slideshow
    """
    implements(IEasySlideshowView)
        
    def getImages(self, slideshowfolderid):
        # we check if there is a folder with id slideshowfolderid
        # if so, we return the images in it
        results = []
        if self.context.getId() == slideshowfolderid or \
           not self.context.isPrincipiaFolderish:
            parent = aq_inner(self.context).getParentNode()
        else:
            parent = self.context
        if slideshowfolderid in parent.objectIds():
            pc = getToolByName(self.context, 'portal_catalog')
            path = {
                'query': 
                '/'.join(parent[slideshowfolderid].getPhysicalPath())
            }
            results = pc.searchResults(portal_type='Image',
                                       path=path,
                                       sort_on='getObjPositionInParent')
        return results
