# # from django.shortcuts import render, redirect, get_object_or_404
# # from .forms import FanlarForms
# # from .models import Fanlar
# # from darsliklar.models import Darsliklar
# #
# # def fanlar_list(request):
# #     fanlar = Fanlar.objects.all()
# #     return render(request, 'fanlar/fanlar_list.html', {'fanlar':fanlar})
# #
# # def fanlar_create(request):
# #     if request.method == 'POST':
# #         form = FanlarForms(request.POST, request.FILES)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('fanlar_list')
# #     else:
# #         form = FanlarForms()
# #     return render(request, 'fanlar/fanlar_create.html', {'form':form})
# #
# # def fanlar_update(request, id):
# #     fanlar = get_object_or_404(Fanlar, id=id)
# #     if request.method == 'POST':
# #         form = FanlarForms(request.POST, request.FILES, instance=fanlar)
# #         if form.is_valid():
# #             form.save()
# #             return redirect('fanlar_list')
# #     form = FanlarForms(instance=fanlar)
# #     return render(request, 'fanlar/fanlar_update.html', {'form':form})
# #
# # def fanlar_delete(request, id):
# #     fanlar = get_object_or_404(Fanlar, id=id)
# #     fanlar.delete()
# #     return redirect('fanlar_list')
# #
# # def darslik_kirish(request, id):
# #     darslik = Darsliklar.objects.all(fan__id=id)
# #     return render(request, 'darsliklar/darsliklar_kirish.html', {'darslik':darslik})
# #
# #
#
# from django.shortcuts import render, redirect, get_object_or_404
# from .forms import FanlarForms
# from .models import Fanlar
# from darsliklar.models import Darsliklar
#
# def fanlar_list(request):
#     fanlar = Fanlar.objects.all()
#     return render(request, 'fanlar/fanlar_list.html', {'fanlar': fanlar})
#
# def fanlar_create(request):
#     if request.method == 'POST':
#         form = FanlarForms(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('fanlar_list')
#     else:
#         form = FanlarForms()
#     return render(request, 'fanlar/fanlar_create.html', {'form': form})
#
# def fanlar_update(request, id):
#     fan = get_object_or_404(Fanlar, id=id)
#     if request.method == 'POST':
#         form = FanlarForms(request.POST, request.FILES, instance=fan)
#         if form.is_valid():
#             form.save()
#             return redirect('fanlar_list')
#     else:
#         form = FanlarForms(instance=fan)
#     return render(request, 'fanlar/fanlar_update.html', {'form': form})
#
# def fanlar_delete(request, id):
#     fan = get_object_or_404(Fanlar, id=id)
#     fan.delete()
#     return redirect('fanlar_list')
#
# def darsliklar_kirish(request, id):
#     darsliklar = Darsliklar.objects.filter(fan_id=id)
#     return render(request, 'darsliklar/darsliklar_kirish.html', {'darslik': darsliklar})
#


from django.shortcuts import render, redirect, get_object_or_404
from .models import Fanlar
from .forms import FanlarForms
from darsliklar.models import Darsliklar

def fanlar_list(request):
    fanlar = Fanlar.objects.all()
    return render(request, 'fanlar/fanlar_list.html', {'fanlar': fanlar})

def fanlar_create(request):
    if request.method == 'POST':
        form = FanlarForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fanlar:fanlar_list')  # DIQQAT: 'fanlar:' qo'shildi
    else:
        form = FanlarForms()
    return render(request, 'fanlar/fanlar_create.html', {'form': form})

def fanlar_update(request, id):
    fan = get_object_or_404(Fanlar, id=id)
    if request.method == 'POST':
        form = FanlarForms(request.POST, request.FILES, instance=fan)
        if form.is_valid():
            form.save()
            return redirect('fanlar:fanlar_list')  # DIQQAT: 'fanlar:' qo'shildi
    else:
        form = FanlarForms(instance=fan)
    return render(request, 'fanlar/fanlar_update.html', {'form': form})

def fanlar_delete(request, id):
    fan = get_object_or_404(Fanlar, id=id)
    fan.delete()
    return redirect('fanlar:fanlar_list')  # DIQQAT: 'fanlar:' qo'shildi (Xatolik shu yerda edi)

def darsliklar_kirish(request, id):
    fan = get_object_or_404(Fanlar, id=id)
    darsliklar = Darsliklar.objects.filter(fan=fan)
    return render(request, 'darsliklar/darsliklar_kirish.html', {'fan': fan, 'darsliklar': darsliklar})