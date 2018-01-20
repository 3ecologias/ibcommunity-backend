from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ClientConfig(AppConfig):
    name = 'client'
    verbose_name = _("Contas de usuário")
    icon = '<i class="material-icons">account_box</i>'
