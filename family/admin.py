from django.contrib import admin
from .models import Family, FamilySources, FamilyPictures, FamilyHealthProblem, FamilyDemography


class FamilyAdmin(admin.ModelAdmin):
    model = Family
    search_fields = ('family_name', 'leader_name', 'email')
    icon = '<i class="material-icons">people_outline</i>'


class FamilySourcesAdmin(admin.ModelAdmin):
    model = FamilySources
    icon = '<i class="material-icons">attach_money</i>'


class FamilyPicturesAdmin(admin.ModelAdmin):
    model = FamilyPictures
    icon = '<i class="material-icons">insert_photo</i>'


class FamilyHealthProblemAdmin(admin.ModelAdmin):
    model = FamilyHealthProblem
    icon = '<i class="material-icons">healing</i>'


class FamilyDemographyAdmin(admin.ModelAdmin):
    model = FamilyDemography
    icon = '<i class="material-icons">trending_up</i>'
    search_fields = ('family__family_name', )


admin.site.register(Family, FamilyAdmin)
admin.site.register(FamilySources, FamilySourcesAdmin)
admin.site.register(FamilyPictures, FamilyPicturesAdmin)
admin.site.register(FamilyHealthProblem, FamilyHealthProblemAdmin)
admin.site.register(FamilyDemography, FamilyDemographyAdmin)