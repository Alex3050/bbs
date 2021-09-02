from django.urls import path

from . import views

urlpatterns = [  # 二级路由
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]