import pickle
import time
from typing import ContextManager
from django.http import response
from django.shortcuts import render
from .models import TblPosts

# Create your views here.

# 接收POST请求数据
def home(request):
    return render(request, "page/home.html")

def send_post(request):
    print(111)
    result = {}
    if request.POST:
        last_time = time.time()
        tag = pickle.dumps(["待分类", ])
        content = pickle.dumps({"content": request.POST["content"]})
        comment = pickle.dumps(["111"])
        new_post = TblPosts(last_time=last_time, tag=tag, content=content, comment=comment)
        new_post.save()
    return render(request, "page/home.html", result)

def get_post(request):
    content = ""
    query_posts = TblPosts.objects.all()
    for post in query_posts:
        if post.id == 9:
            info = pickle.loads(post.content)
            content = info.get("content", "")
    return render(request, "page/home.html", {"read_data": content})