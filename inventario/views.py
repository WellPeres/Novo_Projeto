from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import auth

from usuarios.views import Usuario


# Create your views here.



def index(request):
    """ Tras as receitas registradas e os links para acessos e cadastros """
    users = Usuario.objects.all()
    search = request.GET.get('search')
    if search:
        users = users.filter(nome__icontains=search)
    print(users)
    return render(request, 'index.html', {'users': users})

@login_required
def logout(request):
    """  Realiza o logout de um usuário no sistema"""
    auth.logout(request)
    return redirect('/accounts/logout')

def campo_vazio(campo):
    """ Verifica se os Campos de login ou senha estão preenchidos na hora do cadastro """
    return not campo.strip()

