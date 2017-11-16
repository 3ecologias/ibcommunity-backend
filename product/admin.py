from django.contrib import admin
from .models import Product, ProductCollectionPoint


class ProductAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">spa</i>'


class ProductCollectionPointAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">pan_tool</i>'


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCollectionPoint, ProductCollectionPointAdmin)