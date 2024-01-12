from django.contrib import admin
from .models import Listings, Bids, Comments

# Register your models here.

class ListingsAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "category", "image")


admin.site.register(Listings)
admin.site.register(Bids)
admin.site.register(Comments)