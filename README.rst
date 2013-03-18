=====================
Django CMS team plugin
=====================

Django CMS plugin to list team members/employees.

Example
------------

![Team  plugin example](http://screencloud.net//img/screenshots/cef8f4c816e1cc7e9e1b08339eb3235c.png "Team  plugin example")

Installation
------------

1. Install with pip::

    pip install cmsplugin-team

2. Add `filer` and `cmsplugin_team` to your INSTALLED_APPS in `settings.py`::

    INSTALLED_APPS = (
        ...
        'filer',
        'cmsplugin_team',
    )