"""lvivarc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    # path('obj/1/', views.arcobj, name = 'arcobj'),
    re_path(r'^obj/(?P<obj_id>\d+)/', views.arcobj, name = 'arcobj'),
    re_path(r'^list/(?P<type_id>\d+)/', views.listobj, name = 'listobj'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



