from django.contrib import admin
from .models import Project, ProjectCategory, ProjectPicture


class PictureInline(admin.TabularInline):
    model = ProjectPicture


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        PictureInline
    ]
    search_fields = ['title', 'taxes']
    icon = '<i class="material-icons">library_books</i>'


class ProjectCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    icon = '<i class="material-icons">loyalty</i>'


class ProjectPictureAdmin(admin.ModelAdmin):
    search_fields = ['name']
    icon = '<i class="material-icons">insert_photo</i>'


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(ProjectPicture, ProjectPictureAdmin)