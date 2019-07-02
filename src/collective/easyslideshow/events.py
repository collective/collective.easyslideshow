from collective.easyslideshow.interfaces import ISlideshowCreatedEvent
from collective.easyslideshow.interfaces import ISlideshowRemovedEvent
from collective.easyslideshow.interfaces import ISlideshowWillBeCreatedEvent
from collective.easyslideshow.interfaces import ISlideshowWillBeRemovedEvent
from zope.component.interfaces import ObjectEvent
from zope.interface import implementer


class SlideshowWillBeCreatedEvent(ObjectEvent):
    implementer(ISlideshowWillBeCreatedEvent)


class SlideshowCreatedEvent(ObjectEvent):
    implementer(ISlideshowCreatedEvent)


class SlideshowWillBeRemovedEvent(ObjectEvent):
    implementer(ISlideshowWillBeRemovedEvent)


class SlideshowRemovedEvent(ObjectEvent):
    implementer(ISlideshowRemovedEvent)
