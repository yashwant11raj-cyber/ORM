# Ex02 Django ORM Web Application

# Date: 17/10/2026

# AIM

To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# DESIGN STEPS

## STEP 1:

Clone the problem from GitHub

## STEP 2:

Create a new app in Django project

## STEP 3:

Enter the code for admin.py and models.py

## STEP 4:

Execute Django admin and create details for 10 cars

# PROGRAM

models.py

```
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
```

admin.py

```
from django.contrib import admin
from .models import Zomato, ZomatoAdmin

admin.site.register(Zomato, ZomatoAdmin)
```

settings.py

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app'
]
```

urls.py

```
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', views.index),
    path('about/', views.about),
]
```

# OUTPUT

![alt text](<Screenshot 2026-10-17 160834.png>)
![alt text](<Screenshot 2026-10-17 160904.png>)
![alt text](<Screenshot 2026-10-17 160921.png>)
![alt text](<Screenshot 2026-10-17 160935.png>)

# RESULT

Thus the program for creating a database using ORM hass been executed successfully
