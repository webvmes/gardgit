from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate

# Create your views here.

User = get_user_model()

def registration(request):
    if request.method == "POST":
        username = request.POST .get("username")
        password = request.POST .get("password")
        user = User.objects.create_user(username=username, password=password)

        login(request, user)
        return redirect('index')

    return render(request, 'comptes/registration.html')





def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST .get("password")

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')


    return render(request, 'comptes/connexion.html')




def logout_user(request):
    logout(request)
    return redirect('index')
