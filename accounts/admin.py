from django.contrib import admin
from .models import Profile, Client


class ProfileAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">account_circle</i>'


class ClientAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">account_box</i>'


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Client, ClientAdmin)
