from Products.CMFCore.utils import getToolByName
from plone.indexer import indexer
from Products.ATContentTypes.interface.image import IATImage
from zope.component import provideAdapter


@indexer(IATImage)
def getRelatedLink(obj, **kwargs):
    """Index to get the link for the slide.  It will be the first related
    item.
    """
    if obj.portal_type == 'Image':
        related_items = obj.getRefs('relatesTo')
        if related_items:
            # we're only concerned about the first item
            image_link = related_items[0]
            wftool = getToolByName(obj, 'portal_workflow')
            current_state = wftool.getInfoFor(image_link, 'review_state')
            # we are assuming the linked to object needs to be published
            # TODO: make this configurable.
            if current_state == 'published':
                return '/'.join(image_link.getPhysicalPath()[2:])
    return

provideAdapter(getRelatedLink, name='getRelatedLink')
