"""bet_bola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .views import PunterView, NormalUserView, SellerView, ManagerView, AdminView

app_name = 'user'

router = DefaultRouter()
router.register(r'managers', ManagerView)
router.register(r'sellers', SellerView)
router.register(r'punters', PunterView)
router.register(r'normal-users', NormalUserView)
router.register(r'admins', AdminView)


urlpatterns = router.urls