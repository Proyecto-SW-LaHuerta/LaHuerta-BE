from django.contrib import admin

# Register your models here.
from .models.user import User
from .models.bill import Bill
admin.site.register(User)
admin.site.register(Bill)
