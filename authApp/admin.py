from django.contrib import admin
from .models.bill import Bill
from .models.category import Category
from .models.inventory import Inventory
from .models.paymentType import PaymentType
from .models.product import Product
from .models.provider import Provider
from .models.user import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
        "userId",
        "firstName",
        "lastName",
        "phoneNumber",
        "birthday",
    )
    search_fields = ["firstName", "lastName"]
    list_filter = ("birthday", "phoneNumber")


admin.site.register(User, UserAdmin)
