from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomUserCreationForm

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")  # Redireciona para a home após login
        else:
            messages.error(request, "Usuário ou senha incorretos.")
    
    return render(request, "accounts/login.html")

def logout_view(request):
    logout(request)
    return redirect("index")  # Redireciona para a página de login após logout

def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Salva o usuário no banco
            login(request, user)  # Faz login automaticamente após o cadastro
            return redirect('index')  # Redireciona para a home após o cadastro
    else:
        form = CustomUserCreationForm()  # Formulário em branco para cadastro

    return render(request, 'accounts/register.html', {'form': form})
