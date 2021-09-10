from django.shortcuts import render

# Create your views here.

# 接收POST请求数据
def home(request):
    return render(request, "page/home.html")