from django.contrib import admin
from recordapp.models import Product, Platform, SoldItem, ShippingLocation, Overhead


class SoldItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'platform', 'shipping_location', 'sale_price', 'shipping_cost', 'profit', 'sold_date')
    list_filter = ['sold_date']

class OverheadAdmin(admin.ModelAdmin):
    list_filter = ['date']

admin.site.register(Platform)
admin.site.register(Product)
admin.site.register(ShippingLocation)
admin.site.register(Overhead, OverheadAdmin)
admin.site.register(SoldItem, SoldItemAdmin)
