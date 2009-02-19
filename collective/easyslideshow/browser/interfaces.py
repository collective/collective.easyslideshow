from zope.interface import Interface


class IEasySlideshowBrowserLayer(Interface):
    """Browser layer marker interface
    """ 


class IEasySlideshowLiteBrowserLayer(Interface):
    """Browser layer marker interface for the lite version
    """ 

class IEasySlideshowView(Interface):
    """View class for the Slideshow
    """
    
    def getImages(slideshowfolderid):
        """Get the images for the slideshow based of the given ID
        """

