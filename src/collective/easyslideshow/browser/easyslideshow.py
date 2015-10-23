from Products.CMFPlone import PloneMessageFactory as _
from collective.easyslideshow.browser.interfaces import IEasyslideshowConfiguration
from logging import getLogger
from plone.app.registry.browser import controlpanel

log = getLogger('Plone')


class SlideshowControlPanelForm(controlpanel.RegistryEditForm):

    id = "SlideshowSettings"
    label = _(u"EasySlideshow Settings")
    schema = IEasyslideshowConfiguration
    schema_prefix = "collective.easyslideshow.browser.interfaces.IEasyslideshowConfiguration"


class SlideshowControlPanel(controlpanel.ControlPanelFormWrapper):
    form = SlideshowControlPanelForm
