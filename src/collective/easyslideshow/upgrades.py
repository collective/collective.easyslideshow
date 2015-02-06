try:
    # Plone < 4.3
    from zope.app.component.hooks import getSite
except ImportError:
    # Plone >= 4.3
    from zope.component.hooks import getSite  # NOQA
from logging import getLogger
from p4a.subtyper import interfaces
from p4a.subtyper.sitesetup import unsetup_portal
from Products.CMFCore.utils import getToolByName

from collective.easyslideshow.Extensions.Install import _unregisterUtility
from collective.easyslideshow.interfaces import ISlideshowFolder

logger = getLogger('collective.lineage.upgrades')

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


def removeP4A(context):
    """ remove p4a based descriptors and move to using actions and events
    """
    portal = getSite()
    context.portal_setup.runAllImportStepsFromProfile(
        'profile-collective.easyslideshow:removep4a')
    _unregisterUtility(portal)
    unsetup_portal(portal)

    # really, I mean it p4a, go away
    sm = portal.getSiteManager()

    ########################################################################
    # Get rid of p4a.subtyper utils
    util = sm.queryUtility(interfaces.ISubtyper)
    if util is not None:
        sm.unregisterUtility(provided=interfaces.ISubtyper)
        del util
        sm.utilities.unsubscribe((), interfaces.ISubtyper)
        logger.warn('Force removed interfaces.ISubtyper')

    # Taken from:
    # http://plone.org/documentation/kb/manually-removing-local-persistent-utilities
    provided = sm.utilities._provided
    for x in provided.keys():
        if x.__module__.find("p4a.subtyper") != -1:
            print "deleting %s from utilities" % x
            del provided[x]
    sm.utilities._provided = provided
