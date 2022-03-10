from django.contrib import admin
from .models.bill import Bill
from .models.category import Category
from .models.inventory import Inventory
from .models.paymentType import PaymentType
from .models.product import Product
from .models.provider import Provider
from .models.user import User
from .models.userType import UserType


class BillAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
        "billId",
        "quantity",
        "totalPrice",
        "date",
        "userId",
        "productId",
        "paymentTypeId",
    )
    search_fields = ["quantity", "date"]
    list_filter = ("date", "totalPrice")


class CategoryAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
        "categoryId",
        "categoryType",
        "quantity",
    )
    search_fields = ["categoryType", "quantity"]
    list_filter = ("categoryType", "quantity")


class InventoryAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
        "inventoryId",
        "stock",
        "entryDate",
        "providerId",
        "productId",
    )
    search_fields = ["stock", "entryDate"]
    list_filter = ("stock", "entryDate")


class PaymentTypeAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
        "paymentTypeId",
        "payType",
    )
    search_fields = ["paymentTypeId", "payType"]
    list_filter = ("paymentTypeId", "payType")


class ProductAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
        "productId",
        "name",
        "tax",
        "price",
        "stock",
        "categoryId",
    )
    search_fields = ["name", "price"]
    list_filter = ("tax", "stock")


class ProviderAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
        "providerId",
        "name",
        "phoneNumber",
        "offer",
        "address",
    )
    search_fields = ["name", "phoneNumber"]
    list_filter = ("name", "offer")


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


class UserTypeAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = (
        "userTypeId",
        "userType",
    )
    search_fields = ["userTypeId", "userType"]
    list_filter = ("userTypeId", "userType")


admin.site.register(Bill, BillAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Inventory, InventoryAdmin)
admin.site.register(PaymentType, PaymentTypeAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Provider, ProviderAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserType, UserTypeAdmin)
