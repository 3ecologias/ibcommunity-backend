from django.utils.translation import ugettext_lazy as _
PROVENANCE_TYPE = (
    (_("desconhecida"), _("Desconhecida")),
    (_("natural"), _("Natural")),
    (_("plantio"), _("Plantio")),
    (_("saf"), _("SAF")),
)

COLLECTION_TYPE = (
    (_("area_propria"), _("Área própria")),
    (_("area_compartilhada"), _("Área compartilhada")),
    (_("area_cedida"), _("Área cedida")),
    (_("praia"), _("Praia")),
    (_("rio"), _("Rio")),
)