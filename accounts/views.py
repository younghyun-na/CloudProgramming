from django.contrib import auth
from django.shortcuts import render, redirect


def login(request):
    # 로그인 시키기 (POST 요청)
    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'failed.html')

    # 로그인 폼 (GET 요청)
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
