from zope.interface import implements
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.i18nmessageid import MessageFactory
from zope import schema

from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.vocabularies.catalog import SearchableTextSourceBinder

_ = MessageFactory('collective.easyslideshow')


class ISlideshow(IPortletDataProvider):
    """A portlet for displaying a slideshow

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same
    """

    header = schema.TextLine(
        title=_(u"Portlet header"),
        description=_(u"Title of the rendered portlet"),
        required=True)

    images_location = schema.Choice(
        title=_(u"Images Location"),
        description=_(u"Path to the folder that contains the images "
                       "to be visible in the portlet."),
        required=True,
        source=SearchableTextSourceBinder({'is_folderish': True},
                                          default_query='path:'))

    slideshow_width = schema.Int(
        title=_(u"label_slideshow__portlet_width",
                default=u'Width of the Slideshow Image'),
        description=_(u"help_slideshow_width",
        default=u"Enter a whole number for width in pixels. "
                 "All images should be this width. "
                 "Width should be narrower than the portlet "
                 "column, otherwise you may get unexpected "
                 "results."),
        required=True,
        default=244)

    slideshow_height = schema.Int(
        title=_(u"label_slideshow_portlet_height",
                default=u'Height of the Slideshow Image'),
        description=_(u"help_slideshow_height",
        default=u"Enter a whole number for height in pixels. "
                 "All images should be this height."),
        required=True,
        default=157)

    slide_timeout = schema.Int(
        title=_(u"label_slide_timeout", default=u'Slide Time'),
        description=_(u"help_slide_timeout",
              default=u"Enter a number in milliseconds (5000 = 5 seconds). "
              "Entering '0' will set the slideshow to only be "
              "manually operated using the navigation."),
        required=True,
        default=7000)

    transition = schema.Choice(
        title=_(u"label_transition", default=u'Transition'),
        description=_(u"help_transition",
                      default=u''),
        values=("blindX", "blindY", "blindZ", "cover", "curtainX", "curtainY",
        "fade", "growX", "growY", "scrollUp", "scrollDown",
        "scrollLeft", "scrollRight", "scrollHorz", "scrollVert", "shuffle",
        "slideX", "slideY", "turnUp", "turnDown", "turnLeft", "turnRight",
        "uncover", "wipe", "zoom"),
        default="fade")

    transition_speed = schema.Int(
        title=_(u"label_transition_speed", default=u'Transition Time'),
        description=_(u"help_transition_speed",
            default=u'Enter a number in milliseconds (1000 = 1 second).'),
        required=True,
        default=1000)

    pause_hover = schema.Bool(
        title=_(u"label_pause_hover", default=u'Pause on Hover'),
        description=_(u"help_pause_hover",
                  default=u"If checked, the slideshow will pause when cursor "
                  "is hovering over the slideshow"),
        required=False,
        default=False)

    display_nav = schema.Bool(
        title=_(u"label_display_nav", default=u'Display Navigation'),
        description=_(u"help_display_nav",
                      default=u''),
        required=True,
        default=True)

    display_caption = schema.Bool(
        title=_(u"label_display_caption", default=u'Display Caption'),
        description=_(u"help_display_caption",
                      default=u''),
        required=True,
        default=True)

    random_order = schema.Bool(
        title=_(u"label_random_order", default=u'Random Display Order'),
        description=_(u"help_random_order",
                      default=u''),
        required=True,
        default=False)


class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(ISlideshow)

    def __init__(self, header=u"", images_location=None, slideshow_width=244,
                slideshow_height=157, slide_timeout=7000, transition="fade",
                transition_speed=1000, pause_hover=False, display_nav=True,
                display_caption=True, random_order=False):
        self.header = header
        self.images_location = images_location
        self.slideshow_width = slideshow_width
        self.slideshow_height = slideshow_height
        self.slide_timeout = slide_timeout
        self.transition = transition
        self.transition_speed = transition_speed
        self.pause_hover = pause_hover
        self.display_nav = display_nav
        self.display_caption = display_caption
        self.random_order = random_order

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return "Slideshow Portlet"


class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    render = ViewPageTemplateFile('slideshow.pt')


class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """

    form_fields = form.Fields(ISlideshow)
    label = _(u"title_add_slideshow_portlet",
              default=u"Add slideshow portlet")
    description = _(u"description_slideshow_add_portlet",
                    default=u"A portlet which can display a slideshow. ")

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(ISlideshow)
    ISlideshowlabel = _(u"title_edit_slideshow_portlet",
              default=u"Edit slideshow portlet")
    description = _(u"description_slideshow_edit_portlet",
                    default=u"A portlet which can display a slideshow.")
