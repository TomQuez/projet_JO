from django.contrib import admin

from store.models import Offer,Blog_article,Order,Cart


# Register your models here.
admin.site.register(Offer)
admin.site.register(Blog_article)
admin.site.register(Order)
admin.site.register(Cart)