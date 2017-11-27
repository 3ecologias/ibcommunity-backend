from django.db import models
from django.utils.translation import ugettext_lazy as _
from .constants import SEX_CHOICES


class FamilySources(models.Model):
    source_type = models.CharField(_("Tipo de fonte de renda"), max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Fonte de renda")
        verbose_name_plural = _("Fontes de renda")

    def __str__(self):
        return self.source_type


class FamilyHealthProblem(models.Model):
    health_problem = models.CharField(_("Tipo do problema de saúde"), max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Problema de saúde")
        verbose_name_plural = _("Problemas de saúde")

    def __str__(self):
        return self.health_problem


class Family(models.Model):
    family_name = models.CharField(_("Nome da família"), max_length=255, blank=False)
    interviewee_name = models.CharField(_("Nome do entrevistado"), max_length=255,
                                        blank=True, null=True)
    leader_name = models.CharField(_("Nome do líder da família"), max_length=255,
                                   blank=True, null=True)
    leader_sex = models.CharField(_("Sexo do líder da família"), choices=SEX_CHOICES,
                                  blank=True, null=True)
    leader_phone = models.CharField(_("Telefone do líder da família"), max_length=50,
                                    blank=True, null=True)
    email = models.EmailField(_("Email para contato"), blank=True, null=True)
    occupation = models.TextField(_("Ocupação"), blank=True, null=True,
                                  help_text=_("Descrição da ocupação atual do representante da família"))
    images_license = models.FileField(_("Licença de autorização de uso da imagem"),
                                      upload_to="family/licenses/image/%m/%y", blank=True, null=True)
    future_vision = models.TextField(_("Visão de futuro"), blank=True, null=True,
                                     help_text=_("Descrição da visão de futuro da família"))
    health_problems = models.ManyToManyField(FamilyHealthProblem, verbose_name=_("Problemas de saúde"),
                                             help_text=_("Descrição das doenças crônicas e sobre condições "
                                                         "de saúde da família "))
    incoming_sources = models.ForeignKey(FamilySources, verbose_name=_("Fontes de renda"),
                                              help_text=_("Descrição da principal fonte de renda do "
                                                          "representante da família"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Família (dados gerais)")
        verbose_name_plural = _("Famílias (dados gerais)")
        ordering = ['-created_at']


    def __str__(self):
        return self.family_name


class FamilyPictures(models.Model):
    name = models.CharField(_("Nome da imagem"), max_length=255, blank=False)
    image = models.ImageField(_("Imagem"), upload_to="family/pictures/%y/%m", blank=False)
    community = models.ForeignKey(Family, verbose_name=_("Família"), blank=False,
                                  related_name="images")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Imagem da família")
        verbose_name_plural = _("Imagens das famílias")
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.name

