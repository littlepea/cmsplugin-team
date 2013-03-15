import utils
from django.db import models
from cms.models import CMSPlugin

TEMPLATE_CHOICES = utils.autodiscover_templates()

class EmptyPlugin(CMSPlugin):
    template = models.CharField(max_length=128, choices=TEMPLATE_CHOICES)

    def __unicode__(self):
        return u"empty"
