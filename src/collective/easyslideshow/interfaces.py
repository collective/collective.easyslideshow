from zope.interface import Interface


class ISlideshowFolder(Interface):
    """Content type interface for slideshows
    """

class ISlideshowWillBeCreatedEvent(Interface):
    """An event that is fired before a slideshow is created
    """


class ISlideshowCreatedEvent(Interface):
    """An event that is fired after a slideshow is created
    """


class ISlideshowWillBeRemovedEvent(Interface):
    """An event that is fired before the slideshow is removed
    """


class ISlideshowRemovedEvent(Interface):
    """An event that is fired after a slideshow is removed
    """