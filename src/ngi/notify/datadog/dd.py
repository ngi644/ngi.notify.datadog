# encoding: utf-8
"""
Created on 11/17/14

@author: Takashi NAGAI
"""

__author__ = 'nagai'

import time
from datetime import datetime as dt
from dogapi import dog_http_api as dog
from plone import api


def _get_connect_string():
    """

    :return:
    """
    dd_api_key = api.portal.get_registry_record('ngi.notify.datadog.controlpanel.IDatadog.api_key')
    dd_app_key = api.portal.get_registry_record('ngi.notify.datadog.controlpanel.IDatadog.application_key')
    host_name = api.portal.get_registry_record('ngi.notify.datadog.controlpanel.IDatadog.host_name')
    return dd_api_key, dd_app_key, host_name


def metric_datadog(metric_name, value=1.0, tags={}):
    """
    post to Datadog service
    :param metric_name:
    :param value:
    :param tags:
    :return:
    """

    dd_api_key, dd_app_key, host_name = _get_connect_string()

    if dd_api_key and metric_name:
        dog.api_key = dd_api_key
        dog.application_key = dd_app_key
        dd_pts = value
        dd_tags = [u"{k}:{v}".format(k=k, v=v) for k, v in tags.items()]
        dog.metric(metric_name, dd_pts, host=host_name,
                   tags=dd_tags)


def event_datadog(title, text, date_happened='', tags={}):
    """

    :param title:
    :param text:
    :param date_happened:
    :param tags:
    :return:
    """

    dd_api_key, dd_app_key, host_name = _get_connect_string()

    if not date_happened:
        now = dt.now()
        date_happened = time.mktime(now.timetuple())

    if dd_api_key and title and text:
        dog.api_key = dd_api_key
        dog.application_key = dd_app_key
        dd_tags = [u"{k}:{v}".format(k=k, v=v) for k, v in tags.items()]
        dog.event_with_response(title, text, date_happened=date_happened, tags=dd_tags, host=host_name)
