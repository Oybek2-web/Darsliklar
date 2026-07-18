from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from fanlar.models import SotibOlinganFan
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


@login_required
def darslik_detail(request, id):
    detail = get_object_or_404(Darsliklar, id=id)
    fan = detail.fan

    if fan:
        is_purchased = SotibOlinganFan.objects.filter(user=request.user, fan=fan, tolov_holati=True).exists()
        is_free = not fan.price or fan.price == 0

        if not is_free and not is_purchased:
            messages.error(request, "Ushbu darslikni ko'rish uchun avval fanni sotib olishingiz kerak.")
            return redirect('fanlar:fanlar_list')

    return render(request, 'darsliklar/darslik_detail.html', {'detail': detail})