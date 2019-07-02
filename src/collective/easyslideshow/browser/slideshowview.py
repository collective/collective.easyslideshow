import random

from zope.component import getMultiAdapter
from zope.component import getUtility
from zope.event import notify
from zope.interface import alsoProvides
from zope.interface import implementer
from zope.interface import noLongerProvides

from Acquisition import aq_inner
from plone.folder.interfaces import IFolder
from plone.registry.interfaces import IRegistry
from Products.Five.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import isExpired
from Products.statusmessages.interfaces import IStatusMessage

from collective.easyslideshow.browser.interfaces import IEasySlideshowView, IEasyslideshowConfiguration
from collective.easyslideshow.browser.slideshowmanager import SlideshowManagerAdapter
from collective.easyslideshow.interfaces import ISlideshowFolder
from collective.easyslideshow.events import SlideshowCreatedEvent
from collective.easyslideshow.events import SlideshowRemovedEvent
from collective.easyslideshow.events import SlideshowWillBeCreatedEvent
from collective.easyslideshow.events import SlideshowWillBeRemovedEvent

class SlideshowTool(BrowserView):

    @property
    def available(self):
        """True, if the context can become a slideshow folder.
        """
        return IFolder.providedBy(self.context)

    def disabled(self):
        """True, if context is not a slideshow folder but could possibly be one.
        """
        return self.available and not self.enabled()

    def enabled(self):
        """True, if context is a slideshow folder.
        """
        return ISlideshowFolder.providedBy(self.context)

    def enable(self):
        """Enable a slideshow folder on this context.
        """
        ctx = self.context
        notify(SlideshowWillBeCreatedEvent(ctx))

        # enable slideshow folder
        # folder = self.object
        ctx.setLayout('slideshow_folder_view')
        fol = getToolByName(ctx, 'portal_types')['Folder']
        if 'Slideshow' not in [ac.title for ac in fol.listActions()]:
            fol.addAction("slideshowproperties",
                          "Slideshow",
                          "slideshow_edit_form",
                          "python:object.restrictedTraverse(\
                          '@@plone_interface_info').provides(\
                          'collective.easyslideshow.interfaces.ISlideshowFolder')",
                          "Modify portal content",
                          "folder",)

        # provide ISlideshowFolder
        alsoProvides(ctx, ISlideshowFolder)

        ctx.reindexObject(idxs=('object_provides'))
        notify(SlideshowCreatedEvent(ctx))

        # redirect
        self.request.response.redirect(ctx.absolute_url())

    def disable(self):
        """Disable a slideshow folder on this context.
        """
        ctx = self.context
        notify(SlideshowWillBeRemovedEvent(ctx))

        # remove local site components
        ctx.setLayout('folder_listing')

        # remove ISlideshowFolder
        noLongerProvides(ctx, ISlideshowFolder)

        ctx.reindexObject(idxs=('object_provides'))
        notify(SlideshowRemovedEvent(ctx))

        # redirect
        self.request.response.redirect(ctx.absolute_url())

class SlideshowView(BrowserView):
    """View class for the Slideshow
    """
    implementer(IEasySlideshowView)

    def getImages(self, slideshowfolderid, randomize=False):
        # we check if there is a folder with id slideshowfolderid
        # if so, we return the images in it
        results = []
        if self.context.getId() == slideshowfolderid or \
           not self.context.isPrincipiaFolderish:
            parent = aq_inner(self.context).getParentNode()
        else:
            parent = self.context
        if slideshowfolderid in parent.objectIds():
            pc = getToolByName(self.context, 'portal_catalog')
            path = {
                'query':
                '/'.join(parent[slideshowfolderid].getPhysicalPath())}
            results = pc.searchResults(portal_type='Image',
                                       path=path,
                                       sort_on='getObjPositionInParent')
        if randomize:
            results = [brain for brain in results]
            random.shuffle(results)
        return self.checkForExpired(results)

    def checkForExpired(self, results):
        """Take a list of images, filter out any that are expired
        """
        activeImages = []
        for i in results:
            if not isExpired(i):
                activeImages.append(i)
        return activeImages
    
    def getPortletImages(self, slideshowfolderpath, randomize=False):
        # we check if there is a folder with path
        # slideshowfolderpath
        results = []

        pc = getToolByName(self.context, 'portal_catalog')
        pot_folders = pc.searchResults(UID=slideshowfolderpath)

        if pot_folders:
            folder = pot_folders[0]
            if folder.isPrincipiaFolderish:
                path = {
                    'query': folder.getPath(),
                    'depth': 1,
                }
                results = pc.searchResults(portal_type='Image',
                                           path=path,
                                           sort_on='getObjPositionInParent')
        if randomize:
            results = [brain for brain in results]
            random.shuffle(results)
        return self.checkForExpired(results)


    def getSlideshowLocalProperties(self):
        """ Returns the locally defined properties for the slideshow """
        adapter = SlideshowManagerAdapter(self.context)
        values = adapter.getSlideshowProperties().items()
        props = {}
        for key, value in values:
            props[key] = str(value)
        return props

    def setSlideshowLocalProperties(self):
        """ Saves the locally defined properties for a Slideshow """
        status = IStatusMessage(self.request)
        adapter = SlideshowManagerAdapter(self.context)
        reset_key = []
        for key, value in self.request.form.items():
            if key.startswith('reset_'):
                real_key = key.split('reset_')[1]
                adapter.resetSlideshowProperty(real_key)
                reset_key.append(real_key)
                continue
            if key not in reset_key and value not in ['', 'None']:
                adapter.setSlideshowProperty(key, value)
        status.addStatusMessage('Local slideshow properties have been saved',
                                type='info')
        self.request.response.redirect(self.request.URL.split('@@')[0])

    def getSlideshowGeneralProperties(self):
        """ Returns the slideshow properties defined site-wide """
        prefix = "collective.easyslideshow.browser.interfaces.IEasyslideshowConfiguration"
        # todo: import this list
        pids = ['slideshow_width', 'slideshow_height', 'display_original',
                'slide_timeout', 'transition', 'transition_speed',
                'pause_hover', 'display_nav', 'display_caption',
                'random_order']
        registry = getUtility(IRegistry)

        props = {}
        for pid in pids:
            props[pid] = registry.records['{0}.{1}'.format(prefix, pid)].value
        return props

    def getSlideshowAllProperties(self):
        """ Returns the local property if there is one,
        general property if not """
        local_sp = self.getSlideshowLocalProperties()
        global_sp = self.getSlideshowGeneralProperties()
        for sid in global_sp.keys():
            if sid in local_sp.keys():
                global_sp[sid] = local_sp[sid]
            if type(global_sp[sid]) == tuple:
                global_sp[sid] = global_sp[sid][0]
            if global_sp[sid] == 'True':
                global_sp[sid] = True
            if global_sp[sid] == 'False':
                global_sp[sid] = False
        return global_sp
