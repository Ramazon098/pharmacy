from django.urls import path

from products.views import ProductListAPIView, ProductDetailAPIView, SearchProductAPIView


# Create your urls here.

urlpatterns = [
    path('product/', ProductListAPIView.as_view()),
    path('product/<int:pk>/', ProductDetailAPIView.as_view()),
    path('search-product/', SearchProductAPIView.as_view()),
]
