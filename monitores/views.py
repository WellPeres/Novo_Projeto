from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Monitor
from .forms import MonitorForm

# Create your views here.

@login_required
def monitorList(request):
    """ Tras as receitas registradas e os links para acessos e cadastros """
    telas = Monitor.objects.all()
    print(telas)
    return render(request,'monitores/monitores_list.html', {'telas': telas})

@login_required
def monitorView(request, id):
    views = get_object_or_404(Monitor, pk=id)
    print(views)
    return render(request, 'monitores/monitores_view.html', {'views': views})

@login_required
def newMonitor(request):
    if request.method == 'POST':
        form = MonitorForm(request.POST)

        if form.is_valid():
           views = form.save(commit=False)
           views.save()
           return redirect('monitor_list')

    else:
        form = MonitorForm()
        return render(request, 'monitores/add-monitor.html', {'form' : form })

@login_required
def editMonitor(request, id):
    views = get_object_or_404(Monitor, pk=id)
    form = MonitorForm(instance=views)

    if(request.method == 'POST'):
        form = MonitorForm(request.POST, instance=views)
        if(form.is_valid()):
            views.save()
            return redirect('monitor_list')
        else:
            return render(request, 'monitores/edit-monitor.html', {'form': form, 'views': views})
    else:
        return render(request, 'monitores/edit-monitor.html', {'form': form, 'views': views})