from zope.app.component.hooks import getSite
from Products.CMFCore.utils import getToolByName

def runMigration(context):
    """Run a migration profile as an upgrade step
    """
    portal = getSite()
    setup_tool = getToolByName(portal, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile('profile-collective.easyslideshow:migration-002')