from django.contrib import admin
from .models import CommunityLeadershipType, CommunityLeadership,\
    Community, CommunityContacts, CommunityPicture, CommunitySchools,\
    CommunityBiomes, CommunityBiomesPicture, CommunityCraftwork, CommunityCraftworkPicture


class CommunityContactsInline(admin.TabularInline):
    model = CommunityContacts


class CommunityPictureInline(admin.TabularInline):
    model = CommunityPicture


class CommunitySchoolsInline(admin.TabularInline):
    model = CommunitySchools


class CommunityBiomesInline(admin.StackedInline):
    model = CommunityBiomes


class CommunityCraftworkInline(admin.TabularInline):
    model = CommunityCraftwork


class CommunityCraftworkPictureInline(admin.TabularInline):
    model = CommunityCraftworkPicture


class CommunityAdmin(admin.ModelAdmin):
    inlines = [
        CommunityContactsInline,
        CommunityPictureInline,
        CommunitySchoolsInline,
        CommunityBiomesInline,
        CommunityCraftworkInline,
    ]


class CommunityBiomesPicturesInline(admin.TabularInline):
    model = CommunityBiomesPicture


class CommunityBiomesAdmin(admin.ModelAdmin):
    inlines = [
        CommunityBiomesPicturesInline
    ]


class CommunityCraftworkAdmin(admin.ModelAdmin):
    inlines = [
        CommunityCraftworkPictureInline
    ]


admin.site.register(CommunityLeadershipType)
admin.site.register(CommunityLeadership)
admin.site.register(Community, CommunityAdmin)
admin.site.register(CommunityContacts)
admin.site.register(CommunityPicture)
admin.site.register(CommunitySchools)
admin.site.register(CommunityBiomes, CommunityBiomesAdmin)
admin.site.register(CommunityBiomesPicture)
admin.site.register(CommunityCraftwork, CommunityCraftworkAdmin)
admin.site.register(CommunityCraftworkPicture)