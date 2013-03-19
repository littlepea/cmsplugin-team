=====================
Django CMS team plugin
=====================

Django CMS plugin to list team members/employees.

Installation
------------

1. Install with pip::

    pip install cmsplugin-team

2. Add `filer` and `cmsplugin_team` to your INSTALLED_APPS in `settings.py`::

    INSTALLED_APPS = (
        ...
        # Imperavi (or tinymce) rich text editor is optional
        'imperavi',
        'filer',
        'cmsplugin_team',
    )

3. Install and configure your preferred rich text widget (optional).

Known to work are `django-imperavi`_ as well as for `django-tinymce`_. Be sure to follow installation instructions for respective editors.

For `django-imperavi`_::

    # install
    pip install django-imperavi

    # settings.py
    INSTALLED_APPS = (
        ...
        'imperavi',
    )

    # urls.py
    url(r'^imperavi/', include('imperavi.urls')),


For `django-tinymce`_::

    # install
    pip install django-tinymce

    # settings.py
    INSTALLED_APPS = (
        ...
        'tinymce',
    )

    # urls.py
    url(r'^tinymce/', include('tinymce.urls')),

.. _django-imperavi: https://github.com/vasyabigi/django-imperavi
.. _django-tinycme: https://github.com/aljosa/django-tinymce

Example
------------

.. image:: http://screencloud.net//img/screenshots/cef8f4c816e1cc7e9e1b08339eb3235c.png