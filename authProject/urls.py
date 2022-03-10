from django.contrib import admin
from django.urls import path
from authApp.views.billView import BillListCreateView, BillRetrieveUpdateDestroyView
from authApp.views.categoryView import (
    CategoryListCreateView,
    CategoryRetrieveUpdateDestroyView,
)
from authApp.views.inventoryView import (
    InventoryListCreateView,
    InventoryRetrieveUpdateDestroyView,
)
from authApp.views.paymentTypeView import (
    PaymentTypeListCreateView,
    PaymentTypeRetrieveUpdateDestroyView,
)
from authApp.views.productView import (
    ProductListCreateView,
    ProductRetrieveUpdateDestroyView,
)
from authApp.views.providerView import (
    ProviderListCreateView,
    ProviderRetrieveUpdateDestroyView,
)
from authApp.views.userTypeView import (
    UserTypeListCreateView,
    UserTypeRetrieveUpdateDestroyView,
)
from authApp.views.userView import (
    UserListCreateView,
    UserRetrieveUpdateDestroyView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("bills/", BillListCreateView.as_view()),
    path("bill/<uuid:pk>/", BillRetrieveUpdateDestroyView.as_view()),
    path("categories/", CategoryListCreateView.as_view()),
    path("category/<uuid:pk>/", CategoryRetrieveUpdateDestroyView.as_view()),
    path("inventories/", InventoryListCreateView.as_view()),
    path("inventory/<uuid:pk>/", InventoryRetrieveUpdateDestroyView.as_view()),
    path("paymentTypes/", PaymentTypeListCreateView.as_view()),
    path("paymentType/<uuid:pk>/", PaymentTypeRetrieveUpdateDestroyView.as_view()),
    path("products/", ProductListCreateView.as_view()),
    path("product/<uuid:pk>/", ProductRetrieveUpdateDestroyView.as_view()),
    path("providers/", ProviderListCreateView.as_view()),
    path("provider/<uuid:pk>/", ProviderRetrieveUpdateDestroyView.as_view()),
    path("users/", UserListCreateView.as_view()),
    path("user/<uuid:pk>/", UserRetrieveUpdateDestroyView.as_view()),
    path("userTypes/", UserTypeListCreateView.as_view()),
    path("userType/<uuid:pk>/", UserTypeRetrieveUpdateDestroyView.as_view()),
]
