from cStringIO import StringIO
from Products.CMFCore.utils import getToolByName

def runProfile(portal, profileName):
    setupTool = getToolByName(portal, 'portal_setup')
    setupTool.runAllImportStepsFromProfile(profileName)

def install(portal):
    """Run the GS profile to install this package"""
    out = StringIO()
    runProfile(portal, 'profile-collective.easyslideshow:default')
    print >>out, "Installed collective.easyslideshow"
    return out.getvalue()

def uninstall(portal, reinstall=False):
    """Run the GS profile to uninstall this package"""
    out = StringIO()
    if not reinstall:
        runProfile(portal, 'profile-collective.easyslideshow:uninstall')
        print >>out, "Uninstalled collective.easyslideshow"
    return out.getvalue()
