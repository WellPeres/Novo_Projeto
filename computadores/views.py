from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import Maquinas
from .forms import MaquinaForm

# Create your views here.

def maquinasList(request):
    """ Tras as receitas registradas e os links para acessos e cadastros """
    cpus = Maquinas.objects.all()
    return render(request,'computadores/computadores_list.html', {'cpus': cpus})

def maquinasView(request, id):
    views = get_object_or_404(Maquinas, pk=id)
    print(views)
    return render(request, 'computadores/computadores_views.html', {'views': views})

def newComputador(request):
    if request.method == 'POST':
        form = MaquinaForm(request.POST)

        if form.is_valid():
           views = form.save(commit=False)
           views.status = 'Disponivel'
           views.save()
           return redirect('maquinas_list')

    else:
        form = MaquinaForm()
        return render(request, 'computadores/add-computador.html', {'form' : form })

def editComputador(request, id):
    views = get_object_or_404(Maquinas, pk=id)
    form = MaquinaForm(instance=views)

    if(request.method == 'POST'):
        form = MaquinaForm(request.POST, instance=views)
        if(form.is_valid()):
            views.save()
            return redirect('maquinas_list')
        else:
            return render(request, 'computadores/edit-computador.html', {'form': form, 'views': views})
    else:
        return render(request, 'computadores/edit-computador.html', {'form': form, 'views': views})