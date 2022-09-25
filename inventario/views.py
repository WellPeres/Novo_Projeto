from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages


# Create your views here.

def login(request):
    """ Realiza o login de uma pessoa no sistema """
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            messages.error(request, 'Os campos email e senha não podem ficar em branco')
            return redirect('login')
        print(email, senha)
        if User.objects.filter(email=email).exists():
            email = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=email, password=senha)
            print(email, senha)
            if user is not None:
                auth.login(request, user)
                print('Login realizado com sucesso')
                return redirect('index')
    print('sem sucesso')            
    return render(request, 'login.html')

def index(request):

    return render(request, 'index.html')

def logout(request):
    """  Realiza o logout de um usuário no sistema"""
    auth.logout(request)
    return redirect('index')

def campo_vazio(campo):
    """ Verifica se os Campos de login ou senha estão preenchidos na hora do cadastro """
    return not campo.strip()


