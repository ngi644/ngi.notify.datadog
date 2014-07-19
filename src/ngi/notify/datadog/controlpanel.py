# encoding: utf-8
"""
Created on 07/18/14

@author: Takashi NAGAI
"""

from zope import schema
from zope.interface import Interface
from plone.app.registry.browser import controlpanel
from ngi.notify.datadog import _
    


class IDatadog(Interface):
    """ a Datadog settings """

    api_key = schema.TextLine(
        title=_(u'api_key_title', default = u'api_key'),
        required=True,
        )



class DatadogEditForm(controlpanel.RegistryEditForm):
    """
    Datadog edit form
    """

    schema = IDatadog
    label = _(u'Datadog_label', default=u'Datadog')

    description = _(u'Datadog', default=u'Settings for Datadog')

    def updateWidgets(self):
        super(DatadogEditForm, self).updateWidgets()


class DatadogControlPanel(controlpanel.ControlPanelFormWrapper):
    """
    Datadog Control Panel
    """
    form = DatadogEditForm
