"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import *


urlpatterns = [
    path('', ProductListView.as_view() , name='get_products'),
    path('product/<int:product_id>/', ProductDetailView.as_view(), name='get_product'),
    path('update/<int:product_id>/<int:stock>', update, name='update_product'),
    path('delete/<int:product_id>/', delete, name='delete_product'),
]
