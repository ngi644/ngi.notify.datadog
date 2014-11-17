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


def notify_datadog(metric_name, tags=[]):
    """
    post to Datadog service
    :param metric_name:
    :param tags:
    :return:
    """
    dd_api_key = api.portal.get_registry_record('ngi.notify.datadog.controlpanel.IDatadog.api_key')
    dd_app_key = api.portal.get_registry_record('ngi.notify.datadog.controlpanel.IDatadog.application_key')
    host_name = api.portal.get_registry_record('ngi.notify.datadog.controlpanel.IDatadog.host_name')

    if dd_api_key and metric_name:
        dog.api_key = dd_api_key
        dog.application_key = dd_app_key

        now = dt.now()
        dd_pts = 1.0#(time.mktime(now.timetuple()), 1.0)
        dd_tags = [u"{k}:{v}".format(k=k, v=v) for k, v in tags.items()]
        dog.metric(metric_name, dd_pts, host=host_name,
                   tags=dd_tags)