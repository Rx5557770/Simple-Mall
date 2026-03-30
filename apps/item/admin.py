from django.contrib import admin
from .models import Item, Category, Purchase

class ItemLine(admin.StackedInline):
    model = Item
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ItemLine]
    list_display = ('name', 'is_show')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_show', 'desc', 'price', 'return_url', 'category')


@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'purchased_at')


