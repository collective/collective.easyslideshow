from zope.component import getUtility
from Products.CMFCore.interfaces import IPropertiesTool
from collective.easyslideshow.browser.interfaces import _


def getSlideshowWidth():
    ptool = getUtility(IPropertiesTool)
    return ptool.easyslideshow_properties.getProperty('slideshow_width')


def getSlideshowHeight():
    ptool = getUtility(IPropertiesTool)
    return ptool.easyslideshow_properties.getProperty('slideshow_height')


def getSlideTimeout():
    ptool = getUtility(IPropertiesTool)
    return ptool.easyslideshow_properties.getProperty('slide_timeout')


def getTransition():
    ptool = getUtility(IPropertiesTool)
    return ptool.easyslideshow_properties.getProperty('transition')


def getTransitionSpeed():
    ptool = getUtility(IPropertiesTool)
    return ptool.easyslideshow_properties.getProperty('transition_speed')


def getPauseHover():
    ptool = getUtility(IPropertiesTool)
    return ptool.easyslideshow_properties.getProperty('pause_hover')


def getDisplayNav():
    ptool = getUtility(IPropertiesTool)
    return ptool.easyslideshow_properties.getProperty('display_nav')


def getDisplayCaption():
    ptool = getUtility(IPropertiesTool)
    return ptool.easyslideshow_properties.getProperty('display_caption')

def getRandomOrder():
    ptool = getUtility(IPropertiesTool)
    return ptool.easyslideshow_properties.getProperty('random_order')
