from django.urls import path

from . import views

urlpatterns = [  # 二级路由
    path('home/', views.home, name='home'),
    path('send_post/', views.send_post, name="send_post"),
    path('get_post/', views.get_post, name="get_post"),
]