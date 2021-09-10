from django.urls import path

from . import views

urlpatterns = [  # 二级路由
    path('home/', views.home, name='home'),
]