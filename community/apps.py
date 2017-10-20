from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class CommunityConfig(AppConfig):
    name = 'community'
    verbose_name = _("Comunidades")
