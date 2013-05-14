from zope.component.hooks import getSite
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import base_hasattr

from collective.easyslideshow.interfaces import ISlideshowFolder


def runMigration(context):
    """Run a migration profile as an upgrade step
    """
    portal = getSite()
    setup_tool = getToolByName(portal, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile('profile-collective.easyslideshow:migration-002')

def update_getRelatedLink(context):
    """Update the getRelatedLink index.
    """
    portal = getSite()
    portal_catalog = getToolByName(portal, 'portal_catalog')
    if 'getRelatedLink' not in portal_catalog.indexes():
        return

    result = portal_catalog(portal_type='Image')
    for brain in result:
        img = brain.getObject()
        containing_folder = img.getParentNode()
        if ISlideshowFolder.providedBy(containing_folder):
            img.reindexObject(idxs=['getRelatedLink'])
