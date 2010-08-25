from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import base_hasattr
from collective.easyslideshow.interfaces import ISlideshowFolder
from collective.easyslideshow.browser.slideshowmanager import SlideshowManagerAdapter


def slideLinkSync(obj, event):
    """Need to keep the getRelatedLink up-to-date
    """
    pc = getToolByName(obj, 'portal_catalog')
    # make sure the index exists first
    if 'getRelatedLink' in pc.indexes():
        # check to see if the obj has the attr since this subscriber
        # is applied to all objects, even plone sites.
        if base_hasattr(obj, 'getBRefs'):
            related_items = obj.getBRefs('relatesTo')
            for item in related_items:
                if item.portal_type == 'Image':
                    item.reindexObject(idxs=['getRelatedLink'])


def slideLinkDeleted(obj, event):
    """Need to keep the getRelatedLink up-to-date.  If the item link is being
    removed then we have to find it and re-index those objects.

    manage_beforeDelete kills the refs before IObjectWillBeRemoved is fired.
    So we'll do the clean up after the fact with IObjectRemoved
    """
    pc = getToolByName(obj, 'portal_catalog')
    # make sure the index exists first
    if 'getRelatedLink' in pc.indexes():
        link_path = '/'.join(obj.getPhysicalPath()[2:])
        res = pc(getRelatedLink=link_path)
        for item in res:
            obj = item.getObject()
            obj.reindexObject(idxs=['getRelatedLink'])

def enableSlideshowFolder(event):
    """Slideshow preparation when a slideshow folder is created
    """
    if event.subtype.type_interface == ISlideshowFolder:
        folder = event.object
        folder.setLayout('slideshow_folder_view')
        adapter = SlideshowManagerAdapter(folder)
        fol = getToolByName(folder, 'portal_types')['Folder']
        if 'Slideshow' not in [ac.title for ac in fol.listActions()]:
            fol.addAction("slideshowproperties",
                          "Slideshow",
                          "slideshow_edit_form",
                          "python:object.restrictedTraverse(\
                          '@@plone_interface_info').provides(\
                          'collective.easyslideshow.interfaces.ISlideshowFolder')",
                          "Modify portal content",
                          "folder",)
