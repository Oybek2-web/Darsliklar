# from django.shortcuts import render, redirect, get_object_or_404
# from .forms import DarsliklarForms
# from .models import Darsliklar
#
# def darslik_create(request):
#     if request.method == 'POST':
#         form = DarsliklarForms(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('fanlar:darslik_kirish')
#     form = DarsliklarForms()
#     return render(request, 'darsliklar/darsliklar_create.html', {'form':form})
#
# def darslik_update(request, id):
#     fanlar = get_object_or_404(Darsliklar, id=id)
#     if request.method == 'POST':
#         form = DarsliklarForms(request.POST, request.FILES, instance=fanlar)
#         if form.is_valid():
#             form.save()
#             return redirect('fanlar:darslik_kirish')
#     form = DarsliklarForms(instance=fanlar)
#     return render(request, 'darsliklar/darsliklar_update.html', {'form':form})
#
# def darslik_delete(request, id):
#     darslik = get_object_or_404(Darsliklar, id=id)
#     darslik.delete()
#     return redirect('fanlar:darslik_kirish')


from django.shortcuts import render, redirect, get_object_or_404
from .models import Darsliklar
from .forms import DarsliklarForms


def darslik_create(request):
    if request.method == 'POST':
        form = DarsliklarForms(request.POST, request.FILES)
        if form.is_valid():
            darslik = form.save()
            if darslik.fan:
                return redirect('fanlar:darsliklar_kirish', id=darslik.fan.id)
            return redirect('fanlar:fanlar_list')
    else:
        form = DarsliklarForms()
    return render(request, 'darsliklar/darsliklar_create.html', {'form': form})


def darslik_update(request, id):
    darslik = get_object_or_404(Darsliklar, id=id)
    if request.method == 'POST':
        form = DarsliklarForms(request.POST, request.FILES, instance=darslik)
        if form.is_valid():
            darslik = form.save()
            if darslik.fan:
                return redirect('fanlar:darsliklar_kirish', id=darslik.fan.id)
            return redirect('fanlar:fanlar_list')
    else:
        form = DarsliklarForms(instance=darslik)
    return render(request, 'darsliklar/darsliklar_update.html', {'form': form})


def darslik_delete(request, id):
    darslik = get_object_or_404(Darsliklar, id=id)
    fan_id = darslik.fan.id if darslik.fan else None
    darslik.delete()

    if fan_id:
        return redirect('fanlar:darsliklar_kirish', id=fan_id)
    return redirect('fanlar:fanlar_list')