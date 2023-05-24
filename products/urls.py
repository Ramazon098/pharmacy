from django.urls import path

from products.views import ProductListAPIView, ProductDetailAPIView


# Create your urls here.

urlpatterns = [
    path('products/', ProductListAPIView.as_view()),
    path('product/<int:pk>/', ProductDetailAPIView.as_view()),
]
