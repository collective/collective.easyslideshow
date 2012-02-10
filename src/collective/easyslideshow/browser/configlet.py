from zope.component import adapts, getUtility
from zope.formlib.form import FormFields
from zope.interface import implements
from zope.i18nmessageid import MessageFactory

from Products.CMFCore.interfaces import IPropertiesTool
from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from plone.app.controlpanel.form import ControlPanelForm

from collective.easyslideshow.browser.interfaces import \
        IEasyslideshowConfiguration

_ = MessageFactory('collective.easyslideshow')


class EasyslideshowControlPanelAdapter(SchemaAdapterBase):
    adapts(IPloneSiteRoot)
    implements(IEasyslideshowConfiguration)

    def __init__(self, context):
        super(EasyslideshowControlPanelAdapter, self).__init__(context)
        self.context = getUtility(IPropertiesTool).easyslideshow_properties

    slideshow_width = ProxyFieldProperty(
        IEasyslideshowConfiguration['slideshow_width'])
    slideshow_height = ProxyFieldProperty(
        IEasyslideshowConfiguration['slideshow_height'])
    slide_timeout = ProxyFieldProperty(
        IEasyslideshowConfiguration['slide_timeout'])
    transition = ProxyFieldProperty(
        IEasyslideshowConfiguration['transition'])
    transition_speed = ProxyFieldProperty(
        IEasyslideshowConfiguration['transition_speed'])
    pause_hover = ProxyFieldProperty(
        IEasyslideshowConfiguration['pause_hover'])
    display_nav = ProxyFieldProperty(
        IEasyslideshowConfiguration['display_nav'])
    display_caption = ProxyFieldProperty(
        IEasyslideshowConfiguration['display_caption'])
    random_order = ProxyFieldProperty(
        IEasyslideshowConfiguration['random_order'])


class EasyslideshowControlPanel(ControlPanelForm):
    form_fields = FormFields(IEasyslideshowConfiguration)

    label = _(u"EasySlideshow configuration.")
    description = _(u"Settings to configure the slideshow. "
                    "The slideshow will work best if all images are "
                    "the exact same size, and that size should match "
                    "the width and height below. Otherwise, you may get "
                    "some unexpected behavior based on which transition "
                    "is chosen.")
    form_name = _(u'Slideshow settings')
