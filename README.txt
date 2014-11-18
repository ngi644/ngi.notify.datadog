.. contents::

Introduction
============



Clock server config
--------------------------------------------

zope-conf-additional =
    <clock-server>
        method /plone-instance/@@dd_cron
        period 120
        user user-name
        password password
        host localhost
    </clock-server>