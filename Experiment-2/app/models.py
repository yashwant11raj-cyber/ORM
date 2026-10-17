from django.contrib import admin
from django.db import models


class Zomato(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    phoneno = models.CharField(max_length=10, unique=True, null=False, blank=False)
    email = models.EmailField(max_length=100, unique=True, null=False, blank=False)
    delivery_address = models.TextField(max_length=500, null=False, blank=False)
    delivery_instructions = models.TextField(max_length=500, null=True, blank=True)
    restaurant_name = models.CharField(max_length=100, null=False, blank=False)
    food_item = models.CharField(max_length=100, null=False, blank=False)
    payment_method = models.CharField(max_length=50, null=False, blank=False)
    order_time = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=50, default='Pending')
    order_id = models.CharField(max_length=100, primary_key=True)

class ZomatoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phoneno', 'email', 'delivery_address', 'delivery_instructions', 'restaurant_name', 'food_item', 'payment_method', 'order_time', 'order_status', 'order_id')
    actions = ['mark_as_delivered']
    actions_on_top = True
    actions_selection_counter = True
    readonly_fields = ('order_time',)
    date_hierarchy = 'order_time'
    list_filter = ('order_status', 'restaurant_name', 'food_item', 'payment_method')
    list_per_page = 5
    list_display_links = ['order_id']
    fieldsets = (
        ('Customer Information', {'fields': ('name', 'phoneno', 'email')}),
        ('Delivery Information', {'fields': ('delivery_address', 'delivery_instructions', 'payment_method')}),
        ('Restaurant Information', {'fields': ('restaurant_name', 'food_item')}),
        ('Order Information', {'fields': ('order_time', 'order_status', 'order_id')})
    )