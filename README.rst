=====================
Django CMS empty plugin template
=====================

django-cms plugin template to quickly create your own custom plugins.

Usage
------------

1. Clone the template into your custom directory::

    git clone https://github.com/littlepea/cmsplugin-empty-template.git cmsplugin_your_plugin

2. Change Git origin to your repository::

    cd cmsplugin_your_plugin
    git remote rm origin
    git remote add origin https://github.com/yourname/cmsplugin-your-plugin.git
    git push -u origin master

3. Change `cmsplugin_` directory to your app name::

    mv cmsplugin_ cmsplugin_your_plugin

4. Change `cmsplugin_` to your app name in `setup.py` and `MANIFEST.in`::

5. Change `templates` directories.

6. Change `__init__.py` to set TEMPLATES_SETTING_NAME and TEMPLATES_DIR_NAME if you want to use `autodiscover_templates()` functionality, otherwise just delete `TEMPLATE_CHOICES`, `template` field and `utils.py` from `models.py`.

5. Add your custom code to `models.py` and `cms_plugins.py`, follow `django-cms docs`_ to add your custom plugin code.

.. _django-cms docs: http://docs.django-cms.org/en/develop/extending_cms/custom_plugins.html