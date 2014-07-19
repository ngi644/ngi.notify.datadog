# encoding: utf-8
"""
Created on 07/18/14

@author: Takashi NAGAI
"""

import time
from datetime import datetime as dt
from dogapi import dog_http_api as dog

from five import grok
from zope.lifecycleevent.interfaces import IObjectModifiedEvent
from Products.CMFCore.interfaces import IContentish
from plone import api


@grok.subscribe(IContentish, IObjectModifiedEvent)
def modifiedContent(obj, event):
    """
    Modified Event
    """
    user = api.user.get_current()
    path = '/'.join(obj.getPhysicalPath())
    state = api.content.get_state(obj=obj)
    notify_datadog(user, path, state)


def notify_datadog(user, path='', state=''):
    """
    notify to Datadog service
    :param user:
    :param path:
    :param state:
    :return:
    """
    dd_api_key = api.portal.get_registry_record('ngi.notify.datadog.controlpanel.IDatadog.api_key')
    dd_app_key = api.portal.get_registry_record('ngi.notify.datadog.controlpanel.IDatadog.application_key')
    host_name = api.portal.get_registry_record('ngi.notify.datadog.controlpanel.IDatadog.host_name')

    if not dd_api_key:
        return

    dog.api_key = dd_api_key
    dog.application_key = dd_app_key

    now = dt.now()
    data = (time.mktime(now.timetuple()), 1)

    dog.metric('plone.modified', data, host=host_name,
               tags=['user:%s' % user,
                     'path:%s' % path,
                     'modified',
                     'wf:%s' % state])
