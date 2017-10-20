from django.contrib import admin
from .models import Project, ProjectCategory, ProjectPicture


admin.site.register(Project)
admin.site.register(ProjectCategory)
admin.site.register(ProjectPicture)