from zope.interface import Interface

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('collective.easyslideshow')

class ISlideshowFolder(Interface):
    """Content type interface for slideshows
    """

