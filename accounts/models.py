from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from address.models import Address
from company.models import Company


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("Usuário"),
                                on_delete=models.CASCADE,
                                related_name='profile')
    image = models.ImageField(_("Imagem do perfil"),
                              upload_to='accounts/profile/',
                              blank=True, null=True)
    birth_date = models.DateField(_("Data de nascimento"), blank=False)
    is_support = models.BooleanField(_("Técnico"))
    is_manager = models.BooleanField(_("Gestor"))
    is_admin = models.BooleanField(_("Administrador"))
    address = models.OneToOneField(Address, verbose_name=_("Endereço"),
                                   on_delete=models.CASCADE,
                                   related_name='profile')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Perfil")
        verbose_name_plural = _("Perfis")
        ordering = ['-created_at']

    def __str__(self):
        return self.user.get_full_name()


class Client(models.Model):
    user = models.OneToOneField(User, verbose_name=_("Cliente"),
                                on_delete=models.CASCADE,
                                related_name='client')
    company = models.ForeignKey(Company, verbose_name=_("Empresa"),
                                   on_delete=models.CASCADE,
                                   related_name="clients")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Cliente")
        verbose_name_plural = _("Clientes")
        ordering = ['-created_at']

    def __str__(self):
        return self.user.get_full_name()

