from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib import auth

from usuarios.views import Usuario


# Create your views here.



def index(request):
    """ Tras as receitas registradas e os links para acessos e cadastros """
    users = Usuario.objects.all()
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





def search(request):
    """ Lista as receitas em ordem de Criação por data """
    lista_usuarios = Usuario.objects.order_by().filter()

    if 'search' in request.GET:
        nome_a_buscar = request.GET['search']
        lista_usuarios = lista_usuarios.filter(nome_usuario__icontains=nome_a_buscar)

    return render(request, 'buscar.html', {'users': lista_usuarios})