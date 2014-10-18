from collective.easyslideshow.interfaces import ISlideshowCreatedEvent
from collective.easyslideshow.interfaces import ISlideshowRemovedEvent
from collective.easyslideshow.interfaces import ISlideshowWillBeCreatedEvent
from collective.easyslideshow.interfaces import ISlideshowWillBeRemovedEvent
from zope.component.interfaces import ObjectEvent
from zope.interface import implements


class SlideshowWillBeCreatedEvent(ObjectEvent):
    implements(ISlideshowWillBeCreatedEvent)


class SlideshowCreatedEvent(ObjectEvent):
    implements(ISlideshowCreatedEvent)


class SlideshowWillBeRemovedEvent(ObjectEvent):
    implements(ISlideshowWillBeRemovedEvent)


class SlideshowRemovedEvent(ObjectEvent):
    implements(ISlideshowRemovedEvent)
