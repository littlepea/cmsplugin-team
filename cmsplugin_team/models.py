import utils
from django.db import models
from cms.models import CMSPlugin
from django.utils.translation import ugettext, ugettext_lazy as _
from filer.fields import image


TEMPLATE_CHOICES = utils.autodiscover_templates()

SOCIAL_NETWORK_CHOICES = (
    ('digg', 'Digg'),
    ('dribbble', 'Dribbble'),
    ('facebook', 'Facebook'),
    ('flickr', 'Flickr'),
    ('forrst', 'Forrst'),
    ('google-plus', 'Google+'),
    ('google', 'Google'),
    ('gowalla', 'Gowalla'),
    ('last-fm', 'LastFM'),
    ('linkedin', 'LinkedIn'),
    ('rss', 'RSS'),
    ('share-this', 'ShareThis'),
    ('skype', 'Skype'),
    ('stumbleupon', 'StumbleUpon'),
    ('tumblr', 'Tumblr'),
    ('twitter', 'Twitter'),
    ('vimeo', 'Vimeo'),
    ('you-tube', 'YouTube'),
)


class TeamMember(models.Model):
    """
    Member of a team
    """
    photo = image.FilerImageField(null=True, blank=True, default=None, verbose_name=_('Photo'))
    name = models.CharField(verbose_name=_('Name'), max_length=250)
    position = models.CharField(verbose_name=_('Position'), max_length=250, null=True, blank=True)
    summary = models.TextField(verbose_name=_('Summary'), max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.name


class SocialLink(models.Model):
    """
    Social link
    """
    member = models.ForeignKey(TeamMember, related_name='social_links', verbose_name=_('Member'))
    website = models.CharField(verbose_name=_('Wibsite'), max_length=250, choices=SOCIAL_NETWORK_CHOICES)
    url = models.URLField(verbose_name=_('URL'))

    def __unicode__(self):
        return '%s\'s %s' % (self.member.name, self.website)


class TeamPlugin(CMSPlugin):
    """
    Team plugin
    """
    template = models.CharField(max_length=128, choices=TEMPLATE_CHOICES, verbose_name=_('Template'))
    name = models.CharField(verbose_name=_('Team name'), max_length=250, null=True, blank=True)
    members = models.ManyToManyField(TeamMember, related_name='plugins', verbose_name=_('Members'))

    def __unicode__(self):
        return self.name or ''

    def copy_relations(self, oldinstance):
        self.members = oldinstance.members.all()