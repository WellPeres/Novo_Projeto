from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth, messages

from .forms import UsuarioForm
from .models import Usuario


# Create your views here.


def usuarioList(request):
    """ Tras as receitas registradas e os links para acessos e cadastros """
    users = Usuario.objects.all()
    search = request.GET.get('search')
    if search:
        users = users.filter(nome__icontains=search)
    print(users)
    return render(request,'usuarios/usuario_list.html', {'users': users})

@login_required
def usuarioView(request, id):
    views = get_object_or_404(Usuario, pk=id)
    print(views)
    return render(request, 'usuarios/usuario_view.html', {'views': views})

@login_required
def newUsuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)

        if form.is_valid():
           views = form.save(commit=False)
           views.save()
           messages.info(request, 'Usuário adicionado com sucesso.')
           return redirect('usuario_list')

    else:
        form = UsuarioForm()
        return render(request, 'usuarios/add-usuario.html', {'form' : form })

@login_required
def editUsuario(request, id):
    views = get_object_or_404(Usuario, pk=id)
    form = UsuarioForm(instance=views)

    if(request.method == 'POST'):
        form = UsuarioForm(request.POST, instance=views)
        if(form.is_valid()):
            views.save()
            messages.info(request, 'Usuário editado com sucesso.')
            return redirect('usuario_list')
        else:
            return render(request, 'usuarios/edit-usuario.html', {'form': form, 'views': views})
    else:
        return render(request, 'usuarios/edit-usuario.html', {'form': form, 'views': views})

@login_required
def deleteUsuario(request, id):
    views = get_object_or_404(Usuario, pk=id)
    views.delete()

    messages.info(request, 'Usuário deletado com sucesso.')

    return redirect('')
