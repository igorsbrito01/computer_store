"""computer_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from build_computer import views as views_buil_computer
from userProfile import views as views_user
from django.contrib import auth

admin.site.unregister(auth.models.Group)

router = routers.DefaultRouter()
router.register('computer', views_buil_computer.ComputerViewSet)
router.register('user', views_user.UserViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
