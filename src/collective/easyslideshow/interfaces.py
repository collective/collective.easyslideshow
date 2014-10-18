from zope.interface import Interface


class ISlideshowFolder(Interface):
    """Content type interface for slideshows
    """

class ISlideshowWillBeCreatedEvent(Interface):
    """An event that is fired before a child site is created
    """


class ISlideshowCreatedEvent(Interface):
    """An event that is fired after a child site is created
    """


class ISlideshowWillBeRemovedEvent(Interface):
    """An event that is fired before the child site is removed
    """


class ISlideshowRemovedEvent(Interface):
    """An event that is fired after a child site is removed
    """