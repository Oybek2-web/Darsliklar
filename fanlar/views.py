from django.shortcuts import render, redirect, get_object_or_404
from .forms import FanlarForms
from .models import Fanlar
from darsliklar.models import Darsliklar

def fanlar_list(request):
    fanlar = Fanlar.objects.all()
    return render(request, 'fanlar/fanlar_list.html', {'fanlar':fanlar})

def fanlar_create(request):
    if request.method == 'POST':
        form = FanlarForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fanlar_list')
    form = FanlarForms()
    return render(request, 'fanlar/fanlar_create.html', {'form':form})

def fanlar_update(request, id):
    fanlar = get_object_or_404(id=id)
    if request.method == 'POST':
        form = FanlarForms(request.POST, request.FILES, instance=fanlar)
        if form.is_valid():
            form.save()
            return redirect('fanlar_list')
    form = FanlarForms(instance=fanlar)
    return render(request, 'fanlar/fanlar_update.html', {'form':form})

def fanlar_delete(request, id):
    fanlar = get_object_or_404(id=id)
    fanlar.delete()
    return redirect('fanlar_list')

def darslik_kirish(request, id):
    darslik = Darsliklar.objects.all()
    return render(request, 'darsliklar/darsliklar_list.html', {'darslik':darslik})