from django.contrib import admin
from .models import Home, Card

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')

@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('web_title', 'content')