from django.db import models
from django.utils.translation import ugettext_lazy as _

from .constants import PROVENANCE_TYPE, COLLECTION_TYPE


class ProductCollectionPoint(models.Model):
    location_type = models.CharField(_("Local da coleta/colheita"), max_length=255,
                                     blank=False, choices=COLLECTION_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Local de coleta/colheita")
        verbose_name_plural = _("Locais de coleta/colheita")
        ordering = ["-created_at"]

    def __str__(self):
        return self.location_type


class Product(models.Model):
    scientific_name = models.CharField(_("Nome científico"), max_length=255,
                                       blank=False)
    common_name = models.CharField(_("Nome popular"), max_length=255, blank=False)
    provenance = models.CharField(_("Procedência"), max_length=255, blank=False,
                                  choices=PROVENANCE_TYPE)
    is_threatened = models.BooleanField(_("Espécie ameaçada?"), blank=False)
    fruit_anual_volume = models.PositiveIntegerField(_("Voume anual do fruto"),
                                                     default=0, help_text=_("Em KG"))
    seed_anual_volume = models.PositiveIntegerField(_("Voume anual da semente"),
                                                     default=0, help_text=_("Em KG"))
    pulp_anual_volume = models.PositiveIntegerField(_("Voume anual da polpa"),
                                                     default=0, help_text=_("Em KG"))
    harvest_period = models.TextField(_("Período da safra"), blank=True, null=True,
                                      help_text=_("Informações sobre o período da safra"))
    certification_origin = models.TextField(_("Orgão da certificação"), blank=True,
                                            help_text=_("Informações sobre o orgão que expediu\
                                                        a certificação do produto."))
    benefit_sharing_value = models.TextField(_("Regra de repartição de benefício"), blank=False)
    collection_point = models.OneToOneField(ProductCollectionPoint, verbose_name=_("Local de coleta/colheita"),
                                            related_name='products_collect')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Produto")
        verbose_name_plural = _("Produtos")
        ordering = ["-created_at"]

    def __str__(self):
        return self.common_name