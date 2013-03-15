from django.contrib import admin
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from cmsplugin_team.models import TeamPlugin, TeamMember, SocialLink


class SocialLinkInline(admin.TabularInline):
    model = SocialLink


class TeamMemberAdmin(admin.ModelAdmin):
    inlines = [SocialLinkInline]
    list_display = ['name', 'position']


class CMSTeamPlugin(CMSPluginBase):
    model = TeamPlugin
    name = "Team"

    def render(self, context, instance, placeholder):
        self.render_template = instance.template
        print instance.members.all()
        context.update({
            'instance': instance,
            'members': instance.members.all(),
            'name': instance.name,
        })
        return context

plugin_pool.register_plugin(CMSTeamPlugin)

admin.site.register(TeamMember, TeamMemberAdmin)
