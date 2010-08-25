from cStringIO import StringIO
from Products.CMFCore.utils import getToolByName


def runProfile(portal, profileName):
    setupTool = getToolByName(portal, 'portal_setup')
    setupTool.runAllImportStepsFromProfile(profileName)


def install(portal):
    """Run the GS profile to install this package"""
    out = StringIO()
    runProfile(portal, 'profile-collective.easyslideshow:default')
    # if plone 4 is used, we need to remove the folder icon GS imported
    # to do so we check the python version to see if it is 2.6
    print >> out, "Installed collective.easyslideshow"
    return out.getvalue()


def uninstall(portal, reinstall=False):
    """Remove slideshow_folder_view from display list, reset folder display"""
    if reinstall:
        return
    pt = portal.portal_types
    layout = portal.getProperty("layout")

    pc = getToolByName(portal, 'portal_catalog')
    brains = pc.searchResults(portal_type='Folder')
    for brain in brains:
        folder = brain.getObject()
        if folder.getProperty("layout") is not None:
            if folder.layout == "slideshow_folder_view":
                folder.layout = "folder_listing"

    avViews = []
    for view in pt['Folder'].view_methods:
        if view in ["slideshow_folder_view"]:
            continue
        avViews.append(view)
    pt['Folder'].view_methods = tuple(avViews)

    """Run the GS profile to uninstall this package"""
    out = StringIO()
    runProfile(portal, 'profile-collective.easyslideshow:uninstall')
    print >> out, "Uninstalled collective.easyslideshow"
    return out.getvalue()
