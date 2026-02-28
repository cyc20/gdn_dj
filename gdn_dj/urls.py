"""
URL configuration for gdn_dj project.

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
from django.contrib import admin
from django.urls import path
# 导入刚才写的视图函数（关键：把views.py里的get_nav_items导入进来）
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),  # 后台管理页面（默认）
    # 配置导航栏数据接口的访问路径 ★
    path('api/nav-items/', views.get_nav_items, name='get_nav_items'),
]
