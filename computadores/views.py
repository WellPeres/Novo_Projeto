from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import  messages
from .models import Maquinas
from .forms import MaquinaForm

# Create your views here.

@login_required
def maquinasList(request):
    """ Tras as receitas registradas e os links para acessos e cadastros """
    cpus = Maquinas.objects.all()
    return render(request,'computadores/computadores_list.html', {'cpus': cpus})

@login_required
def maquinasView(request, id):
    views = get_object_or_404(Maquinas, pk=id)
    print(views)
    return render(request, 'computadores/computadores_views.html', {'views': views})

@login_required
def newComputador(request):
    if request.method == 'POST':
        form = MaquinaForm(request.POST)

        if form.is_valid():
           views = form.save(commit=False)
           views.status = 'Disponivel'
           views.save()
           messages.info(request, 'Computador adicionado com sucesso.')
           return redirect('maquinas_list')
    else:
        form = MaquinaForm()
        return render(request, 'computadores/add-computador.html', {'form' : form })

@login_required
def editComputador(request, id):
    views = get_object_or_404(Maquinas, pk=id)
    form = MaquinaForm(instance=views)

    if(request.method == 'POST'):
        form = MaquinaForm(request.POST, instance=views)
        if(form.is_valid()):
            views.save()
            messages.info(request, 'Computador editado com sucesso.')
            return redirect('maquinas_list')
        else:
            return render(request, 'computadores/edit-computador.html', {'form': form, 'views': views})
    else:
        return render(request, 'computadores/edit-computador.html', {'form': form, 'views': views})