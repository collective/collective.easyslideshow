from cStringIO import StringIO
from Products.CMFCore.utils import getToolByName
from zope.component import getUtility
from Products.CMFCore.interfaces import IPropertiesTool
from zope.interface import noLongerProvides
from p4a.subtyper import interfaces as p4ainterfaces
from collective.easyslideshow import interfaces as essinterfaces
from zope.annotation.interfaces import IAnnotations
from zope.component import getMultiAdapter
from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.portlets.interfaces import IPortletManager


def runProfile(portal, profileName):
    setupTool = getToolByName(portal, 'portal_setup')
    setupTool.runAllImportStepsFromProfile(profileName)


def install(portal):
    """Run the GS profile to install this package"""
    out = StringIO()
    # we have our default settings in the initial profile.
    # we check if they are setup and if not, we run the
    # inital profile
    ptool = getUtility(IPropertiesTool)
    if not ptool.get("easyslideshow_properties"):
        runProfile(portal, 'profile-collective.easyslideshow:initial')
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

    pc = getToolByName(portal, 'portal_catalog')
    brains = pc.searchResults(portal_type='Folder')
    for brain in brains:
        folder = brain.getObject()
        if folder.getProperty("layout") is not None:
            if folder.layout == "slideshow_folder_view":
                folder.layout = "folder_listing"
        noLongerProvides(folder, p4ainterfaces.ISubtyped)
        noLongerProvides(folder, essinterfaces.ISlideshowFolder)
        annotations = IAnnotations(folder)
        if annotations.get('easyslideshow.slideshowmanager.props'):
            annotations.pop('easyslideshow.slideshowmanager.props')
        psD = annotations.get('p4a.subtyper.DescriptorInfo')
        if psD and psD.get('descriptor_name')\
           and psD['descriptor_name'] == 'collective.easyslideshow.slideshow':
            annotations.pop('p4a.subtyper.DescriptorInfo')
    allbrains = pc()
    for brain in allbrains:
        item = brain.getObject()
        for column in ['plone.leftcolumn', 'plone.rightcolumn']:
            manager = getUtility(IPortletManager, name=column)
            assignments = getMultiAdapter((item, manager),
                                                 IPortletAssignmentMapping)
            for key in assignments.keys():
                if key.startswith('slideshow-portlet'):
                    del assignments[key]

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
