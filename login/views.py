from django.db.models import query
from django.shortcuts import render
from .models import TblUser

# Create your views here.

# 接收POST请求数据
def login(request):
    info ={}
    if request.POST:
        info["uname"] = request.POST["username"]
        info["psword"] = request.POST["password"]
        info["result"] = "没有这个用户"
        query_result = TblUser.objects.all()
        print(info)
        for user in query_result:
            if user.username == request.POST["username"] and \
               user.password == request.POST["password"]:
                info["result"] = "有这个用户"
    return render(request, "login/login.html", info)

def register(request):
    info ={}
    if request.POST:
        uname = request.POST["username"]
        psword = request.POST["password"]
        check_psword = request.POST["check_password"]
        if psword != check_psword:
            info["result"] = "密码与确认密码不一致"
        else:  # TODO lyl 增加已有账号检查
            new_user = TblUser(username=uname, password=psword)
            new_user.save()
            info["result"] = "注册成功"
        info["uname"] = uname
        info["psword"] = psword
        info["check_psword"] = check_psword
    return render(request, "login/register.html", info)

