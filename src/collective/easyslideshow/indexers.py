from Products.CMFCore.utils import getToolByName
from plone.app.contenttypes.interfaces import IImage
from plone.indexer import indexer
from Products.ATContentTypes.interface.image import IATImage
from Products.CMFPlone.utils import base_hasattr
from zope.component import provideAdapter

import pkg_resources

try:
    pkg_resources.get_distribution('plone.app.relationfield')
except pkg_resources.DistributionNotFound:
    HAS_RELATIONFIELD = False
else:
    from plone.app.relationfield.behavior import IRelatedItems
    HAS_RELATIONFIELD = True


@indexer(IImage)
def getRelatedLink(obj, **kwargs):
    """Index to get the link for the slide.  It will be the first related
    item.
    """

    # Archetypes
    if base_hasattr(obj, 'getRawRelatedItems'):
        related_items = obj.getRefs('relatesTo')
        if related_items:
            # we're only concerned about the first item
            return checkPermissions(obj, related_items[0])

    # Dexterity
    if HAS_RELATIONFIELD and IRelatedItems.providedBy(obj):
        related_items = obj.relatedItems
        if related_items:
            # we're only concerned about the first item
            return checkPermissions(obj, related_items[0])

    raise AttributeError


def checkPermissions(obj, related):
    """check that the linked item is published
    """
    catalog = getToolByName(obj, 'portal_catalog')
    brain = catalog(path=dict(query=related.to_path, depth=0))
    return brain[0].getURL()


provideAdapter(getRelatedLink, name='getRelatedLink')