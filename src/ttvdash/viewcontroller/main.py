from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return render(request,'pages/main.html')

def login_view(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request,'wrong username and password')
            return redirect('login')
    else:
        return render(request, 'pages/login.html')