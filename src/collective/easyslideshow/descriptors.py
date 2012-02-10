from zope import interface
from p4a.subtyper import interfaces as stifaces
from collective.easyslideshow import interfaces


class SlideshowDescriptor(object):
    """A descriptor for the Slideshow subtype.
    """

    interface.implements(stifaces.IPortalTypedFolderishDescriptor)
    title = 'Slideshow'
    description = 'An Image Slideshow'
    type_interface = interfaces.ISlideshowFolder
    for_portal_type = 'Folder'
