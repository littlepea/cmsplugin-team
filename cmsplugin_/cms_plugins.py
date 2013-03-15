from django.contrib import admin
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from cmsplugin_.models import EmptyPlugin

class CMSEmptyPlugin(CMSPluginBase):
    model = EmptyPlugin
    name = "Empty"

    def render(self, context, instance, placeholder):
        self.render_template = instance.template
        context.update({
            'instance': instance,
        })
        return context
plugin_pool.register_plugin(CMSEmptyPlugin)
