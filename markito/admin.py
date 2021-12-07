from django.contrib import admin
from .models import Categories, Products,Channel,Store


# Register your models here.
class ChannelAdmin(admin.ModelAdmin):
    pass

class StoreAdmin(admin.ModelAdmin):
    pass

class CategoriesAdmin(admin.ModelAdmin):
    pass

class ProductsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Channel,ChannelAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(Categories,CategoriesAdmin)
admin.site.register(Products,ProductsAdmin)