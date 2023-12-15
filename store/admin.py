from django.contrib import admin

from store.models import Offer,Blog_article,Order,Cart,Ticket

class OfferAdmin(admin.ModelAdmin):
    """Personnalisation de l'interface d'administration."""
    list_display   = ('name', 'price', 'stock','sales_number')


class Blog_articleAdmin(admin.ModelAdmin):
    """Personnalisation de l'interface d'administration."""
    list_display   = ('title', 'description')

class OrderAdmin(admin.ModelAdmin):
    """Personnalisation de l'interface d'administration."""
    list_display   = ('user', 'offer', 'quantity','ordered','ordered_date')
    
    
class TicketAdmin(admin.ModelAdmin):
    """Personnalisation de l'interface d'administration."""
    list_display   = ('user', 'ticket_name')


"""Enregistre les modèles dans l'interface d'administration."""
admin.site.register(Offer, OfferAdmin)
admin.site.register(Blog_article, Blog_articleAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Cart)
admin.site.register(Ticket, TicketAdmin)