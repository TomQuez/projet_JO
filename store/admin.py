from django.contrib import admin

from store.models import Offer,Blog_article,Order,Cart,Ticket



"""Enregistre les modèles dans l'interface d'administration."""
admin.site.register(Offer)
admin.site.register(Blog_article)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Ticket)