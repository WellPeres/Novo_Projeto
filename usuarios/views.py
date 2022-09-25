from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages

from .forms import UsuarioForm
from .models import Usuario


# Create your views here.

def usuarioList(request):
    """ Tras as receitas registradas e os links para acessos e cadastros """
    users = Usuario.objects.all()
    print(users)
    return render(request,'usuarios/usuario_list.html', {'users': users})

def usuarioView(request, id):
    views = get_object_or_404(Usuario, pk=id)
    print(views)
    return render(request, 'usuarios/usuario_view.html', {'views': views})

def newUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
           views = form.save(commit=False)
           views.save()
           return redirect('usuario_list')

    else:
        form = UsuarioForm()
        return render(request, 'usuarios/add-usuario.html', {'form' : form })


def editUsuario(request, id):
    views = get_object_or_404(Usuario, pk=id)
    form = UsuarioForm(instance=views)

    if(request.method == 'POST'):
        form = UsuarioForm(request.POST, instance=views)
        if(form.is_valid()):
            views.save()
            return redirect('usuario_list')
        else:
            return render(request, 'usuarios/edit-usuario.html', {'form': form, 'views': views})
    else:
        return render(request, 'usuarios/edit-usuario.html', {'form': form, 'views': views})
