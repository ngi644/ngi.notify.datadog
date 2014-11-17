# encoding: utf-8
"""
Created on 07/18/14

@author: Takashi NAGAI
"""
from zope.interface import Interface
from five import grok
from zope.lifecycleevent.interfaces import (IObjectCreatedEvent,
                                            IObjectModifiedEvent)
from Products.CMFCore.interfaces import IContentish
from Products.PlonePAS.events import (UserInitialLoginInEvent,
                                      UserLoggedInEvent,
                                      UserLoggedOutEvent)

from plone import api

from ngi.notify.datadog.dd import notify_datadog


@grok.subscribe(IContentish, IObjectCreatedEvent)
def createdContent(obj, event):
    """
    Created Event
    """
    user = api.user.get_current()
    path = '/'.join(obj.getPhysicalPath())
    state = api.content.get_state(obj=obj)
    portal_type = obj.portal_type
    content_type = obj.Type()
    metric_name = 'plone.created'
    tags = dict(user=user.id,
                path=path,
                content_type=content_type,
                portal_type=portal_type,
                action='object_created',
                workflow=state)
    notify_datadog(metric_name, tags)


@grok.subscribe(IContentish, IObjectModifiedEvent)
def modifiedContent(obj, event):
    """
    Modified Event
    """
    user = api.user.get_current()
    path = '/'.join(obj.getPhysicalPath())
    state = api.content.get_state(obj=obj)
    portal_type = obj.portal_type
    content_type = obj.Type()
    metric_name = 'plone.modified'
    tags = dict(user=user.id,
                path=path,
                content_type=content_type,
                portal_type=portal_type,
                action='object_modified',
                workflow=state)
    notify_datadog(metric_name, tags)


def _log_in_out(metric_name, action):
    """

    :param metric_name:
    :param action:
    :return:
    """
    user = api.user.get_current()
    path = '/'.join(obj.getPhysicalPath())
    metric_name = metric_name
    tags = dict(user=user.id,
                path=path,
                action=action)
    notify_datadog(metric_name, tags)


@grok.subscribe(Interface, UserLoggedInEvent)
def loggedIn(obj, event):
    """
    logged_out event
    :param obj:
    :param event:
    :return:
    """
    _log_in_out(u'plone.login', u'login')


@grok.subscribe(Interface, UserLoggedOutEvent)
def loggedOut(obj, event):
    """
    logged_out event
    :param obj:
    :param event:
    :return:
    """
    _log_in_out(u'plone.logout', u'logout')