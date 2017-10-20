from django.db import models
from django.utils.translation import ugettext_lazy as _

from community.models import Community


class Project(models.Model):
    name = models.CharField(_("Nome"), max_length=255, blank=False)
    target_area = models.TextField(_("Área de atuação"), blank=False)
    theme_description = models.TextField(_("Tema"), blank=False)
    goals = models.TextField(_("Objetivos"), blank=False)
    specific_goals = models.TextField(_("Objetivos específicos"), blank=True, null=True)
    activities = models.TextField(_("Atividades a serem desenvolvidas"), blank=False)
    results = models.TextField(_("Resultados esperados"), blank=False)
    schedule = models.FileField(_("Cronograma"),
                                upload_to="project/schedules/%y/%m",
                                blank=False,
                                help_text=_("Arquivo PDF com o cronograma do projeto"))
    target_audience = models.TextField(_("Público alvo"), blank=False)
    budget = models.FileField(_("Orçamento"),
                              upload_to="project/budgets/%y/%m",
                              blank=False,
                              help_text=_("Aquivo PDF com o orçamento do projeto"))
    project_totals = models.DecimalField(_("Valor total do projeto"),
                                         max_digits=20,
                                         decimal_places=2,
                                         blank=False)
    taxes = models.DecimalField(_("Valor do administrativo"),
                                max_digits=5,
                                decimal_places=2,
                                blank=False,
                                help_text="Percentagem do valor do projeto que será\
                                 destinado ao administrativo")
    community_tour = models.BooleanField(_("Visita comunitária"),
                                         blank=False,
                                         help_text=_("Assinala caso seja projeto de visita\
                                                     comunitária"))
    future_vision = models.TextField(_("Visão de futuro"),
                                     blank=False,
                                     help_text=_("Breve resumo de qual seria a visão de futuro \
                                                 da comunidade com a execução do projeto."))

    category = models.ManyToManyField(ProjectCategory, verbose_name=_("Categorias"),
                                      related_name="category_projects")
    community = models.ForeignKey(Community, verbose_name=_("Comunidade"), related_name="community_projects")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Projeto")
        verbose_name_plural = _("Projetos")
        ordering = ["-created_at"]

    def __str__(self):
        return self.name


class ProjectCategory(models.Model):
    name = models.CharField(_("Nome"), max_length=255, blank=False, unique=True)

    class Meta:
        verbose_name = _("Categoria de projeto")
        verbose_name_plural = _("Categorias de projeto")


class ProjectPicture(models.Model):
    name = models.CharField(_("Nome da imagem"), max_length=255, blank=False)
    image = models.ImageField(_("Imagem"), upload_to="project/pictures/%y/%m", blank=False)
    project = models.ForeignKey(Project, verbose_name=_("Project"), blank=False,
                                related_name="images")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Imagem do projeto")
        verbose_name_plural = _("Imagens do projeto")
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.name