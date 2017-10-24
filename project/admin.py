from django.contrib import admin
from .models import Project, ProjectCategory, ProjectPicture


class PictureInline(admin.TabularInline):
    model = ProjectPicture


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        PictureInline
    ]


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory)
admin.site.register(ProjectPicture)