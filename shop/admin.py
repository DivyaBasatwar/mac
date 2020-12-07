from django.contrib import admin

from .models import product, Contact, Orders, OrderUpdate   #product is the table we have created in models.py

# Register your models here.
admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
