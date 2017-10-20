from django.contrib import admin
from .models import CommunityLeadershipType, CommunityLeadership,\
    Community, CommunityContacts, CommunityPicture, CommunitySchools,\
    CommunityBiomes, CommunityBiomesPicture

admin.site.register(CommunityLeadershipType)
admin.site.register(CommunityLeadership)
admin.site.register(Community)
admin.site.register(CommunityContacts)
admin.site.register(CommunityPicture)
admin.site.register(CommunitySchools)
admin.site.register(CommunityBiomes)
admin.site.register(CommunityBiomesPicture)