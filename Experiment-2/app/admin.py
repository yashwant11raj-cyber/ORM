from django.contrib import admin
from .models import Zomato, ZomatoAdmin

admin.site.register(Zomato, ZomatoAdmin)
