from django.contrib import admin
from .models import Order
# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('trade_id', 'order_id', 'amount', 'payment', 'create_at', 'pay_time', 'status', 'item', 'user')