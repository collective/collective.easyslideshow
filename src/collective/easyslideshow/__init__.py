from Products.CMFPlone.CatalogTool import registerIndexableAttribute
from Products.CMFCore.utils import getToolByName

def initialize(context):

    def getRelatedLink(obj, portal, **kwargs):
        """Index to get the link for the slide.  It will be the first related
        item.
        """
        if obj.portal_type == 'Image':
            related_items = obj.getRefs('relatesTo')
            if related_items:
                # we're only concerned about the first item
                image_link = related_items[0]
                wftool = getToolByName(portal, 'portal_workflow')
                current_state = wftool.getInfoFor(image_link, 'review_state')
                # we are assuming the linked to object needs to be published
                # TODO: make this configurable.
                if current_state == 'published':
                    return '/'.join(image_link.getPhysicalPath()[2:])
        return

    registerIndexableAttribute('getRelatedLink', getRelatedLink)
