.. contents::

Introduction
============

Notify events to DataDog

Supported events
-------------------------------------------

- Zope process start.

- Content {create, modify, and change workflow}.

- User {add, delete, login and logout}.

- Site settings modify.

- ZODB size(using Zope clock server).



Usage
--------------------------------------------

Add the following to your buildout:

::

  [buildout]

  eggs =
      ngi.notify.datadog


  [instance]

  zope-conf-additional =
      <clock-server>
          method /your-plone-instance/@@dd_cron
          period 120
          user your-admin-user-name
          password your-admin-user-password
          host localhost
      </clock-server>


Install via quickinstaller or the Add Ons control panel.

