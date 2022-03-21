from django.contrib import admin
from django.urls import URLPattern, path
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
    ProductRetrieveUpdateDestroyView, ProductPicture, CreateProduct
)
from authApp.views.providerView import (
    ProviderListCreateView,
    ProviderRetrieveUpdateDestroyView,
)
from authApp.views.userView import UserCreateView, UserDetailView, UserListCreateView
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path("bills/", BillListCreateView.as_view()),
    path("bill/<uuid:pk>/", BillRetrieveUpdateDestroyView.as_view()),
    path("categories/", CategoryListCreateView.as_view()),
    path("category/<uuid:pk>/", CategoryRetrieveUpdateDestroyView.as_view()),
    path("inventories/", InventoryListCreateView.as_view()),
    path("inventory/<uuid:pk>/", InventoryRetrieveUpdateDestroyView.as_view()),
    path("paymentTypes/", PaymentTypeListCreateView.as_view()),
    path("paymentType/<uuid:pk>/", PaymentTypeRetrieveUpdateDestroyView.as_view()),
    path("products/", ProductListCreateView.as_view()),
    path("product/creation/", CreateProduct.as_view()),
    path("product/<uuid:pk>/", ProductRetrieveUpdateDestroyView.as_view()),
    path("providers/", ProviderListCreateView.as_view()),
    path("provider/<uuid:pk>/", ProviderRetrieveUpdateDestroyView.as_view()),
    path('user/', UserCreateView.as_view()),
    path('users/', UserListCreateView.as_view()),
    path('user/<uuid:pk>/', UserDetailView.as_view()),
    path('ProductPicture/', ProductPicture.as_view()),
    
]

urlpatterns +=  static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)