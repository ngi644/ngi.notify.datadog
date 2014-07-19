
from zope.i18nmessageid import MessageFactory

MessageFactory = MessageFactory('ngi.notify.datadog')
_ = MessageFactory


def initialize(context):
    """Initializer called when used as a Zope 2 product."""
