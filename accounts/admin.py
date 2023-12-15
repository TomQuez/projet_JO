from django.contrib import admin
from .models import Shopper
# Register your models here.

class ShopperAdmin(admin.ModelAdmin):
    list_display   = ('last_name', 'first_name','email','is_staff','is_superuser','is_active')
    list_filter    = ('is_staff','is_superuser','is_active','groups')

admin.site.register(Shopper,ShopperAdmin)