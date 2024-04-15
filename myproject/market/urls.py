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
from django.views.generic.base import RedirectView
from django.conf.urls import url

urlpatterns = [
    path('by_category/<int:category_id>/', by_category, name='by_category'),
    path('by_author/<int:author_id>/', by_author, name='by_author'),
    path('product/<int:product_id>/', product, name='product'),
    path('json_request/', json_request, name='json_request'),
    path('json_request_with_serialization/', json_request_with_serialization, name='json_request_with_serialization'),
    path('json_request_with_values_list/', json_request_with_values_list, name='json_request_with_values_list'),
    path('json_request_with_serialization_framework/', json_request_with_serialization_framework,
         name='json_request_with_serialization_framework'),
    path('', index, name='index'),
    path('add_author/', AuthorCrateView.as_view(), name='add_author'),
    path('add_book/', BookCrateView.as_view(), name='add_book'),
    path('add_category/', CategoryCrateView.as_view(), name='add_category'),
    path('test/', test, name='test'),
    # Other URL patterns
    path('i18n/', RedirectView.as_view(url='/')),
    url(r'^set_language/$', 'django.views.i18n.set_language', name='set_language'),



    # path('<path:route>/', default_route, name='default_route'),
]
