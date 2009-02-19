from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import base_hasattr

def slideLinkSync(self, event):
    """Need to keep the getRelatedLink up-to-date
    """
    obj = event.object
    # check to see if the obj has the attr since this subscriber
    # is applied to all objects, even plone sites.
    if base_hasattr(obj, 'getBRefs'):
        related_items = obj.getBRefs('relatesTo')
        for item in related_items:
            if item.portal_type == 'Image':
                item.reindexObject(idxs=['getRelatedLink'])

def slideLinkDeleted(self, event):
    """Need to keep the getRelatedLink up-to-date.  If the item link is being
    removed then we have to find it and re-index those objects.
    
    manage_beforeDelete kills the refs before IObjectWillBeRemoved is fired.
    So we'll do the clean up after the fact with IObjectRemoved
    """
    obj = event.object
    link_path = '/'.join(obj.getPhysicalPath()[2:])
    pc = getToolByName(obj, 'portal_catalog')
    res = pc(getRelatedLink=link_path)
    for item in res:
        obj = item.getObject()
        obj.reindexObject(idxs=['getRelatedLink'])
