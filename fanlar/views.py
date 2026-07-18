from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Fanlar, SotibOlinganFan
from .forms import FanlarForms
from darsliklar.models import Darsliklar
from django.contrib import messages

def fanlar_create(request):
    if request.method == 'POST':
        form = FanlarForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('fanlar:fanlar_list')
    else:
        form = FanlarForms()
    return render(request, 'fanlar/fanlar_create.html', {'form': form})



def fanlar_update(request, id):
    fan = get_object_or_404(Fanlar, id=id)
    if request.method == 'POST':
        form = FanlarForms(request.POST, request.FILES, instance=fan)
        if form.is_valid():
            form.save()
            return redirect('fanlar:fanlar_list')
    else:
        form = FanlarForms(instance=fan)
    return render(request, 'fanlar/fanlar_update.html', {'form': form})

def fanlar_delete(request, id):
    fan = get_object_or_404(Fanlar, id=id)
    fan.delete()
    return redirect('fanlar:fanlar_list')

@login_required
def fan_sotib_olish(request, id):
    fan = get_object_or_404(Fanlar, id=id)

    # Agar fan bepul bo'lsa, to'g'ridan-to'g'ri darslikka yo'naltiramiz
    if not fan.price or fan.price == 0:
        return redirect('fanlar:darsliklar_kirish', id=fan.id)

    # Foydalanuvchi allaqachon sotib olganini tekshiramiz
    already_purchased = SotibOlinganFan.objects.filter(user=request.user, fan=fan, tolov_holati=True).exists()

    if already_purchased:
        messages.info(request, "Siz bu fanni allaqachon sotib olgansiz.")
        return redirect('fanlar:darsliklar_kirish', id=fan.id)

    # DIQQAT: Bu yerda haqiqiy loyihada Click yoki Payme API'si chaqiriladi.
    # Hozircha test qilish uchun to'lovni avtomatik tasdiqlaymiz:
    SotibOlinganFan.objects.create(user=request.user, fan=fan, tolov_holati=True)
    messages.success(request, f"'{fan.title}' fani muvaffaqiyatli sotib olindi!")

    return redirect('fanlar:darsliklar_kirish', id=fan.id)


@login_required
def darsliklar_kirish(request, id):
    fan = get_object_or_404(Fanlar, id=id)

    # Foydalanuvchi fanni sotib olganmi yoki fan bepulmi?
    is_purchased = SotibOlinganFan.objects.filter(user=request.user, fan=fan, tolov_holati=True).exists()
    is_free = not fan.price or fan.price == 0

    if not is_free and not is_purchased:
        # Sotib olmagan bo'lsa, faqat fanning qisqacha ma'lumoti va "Sotib olish" tugmasi ko'rsatiladi
        return render(request, 'fanlar/fan_detail.html', {'fan': fan, 'is_purchased': False})

    # Sotib olgan yoki bepul bo'lsa, darsliklarni ko'rsatamiz
    darsliklar = Darsliklar.objects.filter(fan=fan)
    return render(request, 'darsliklar/darsliklar_kirish.html', {
        'fan': fan,
        'darsliklar': darsliklar,
        'is_purchased': True
    })


def fanlar_list(request):
    fanlar = Fanlar.objects.all()
    purchased_fan_ids = []

    # Agar foydalanuvchi tizimga kirgan bo'lsa, u sotib olgan fanlar ID larini olamiz
    if request.user.is_authenticated:
        purchased_fan_ids = SotibOlinganFan.objects.filter(
            user=request.user, tolov_holati=True
        ).values_list('fan_id', flat=True)

    return render(request, 'fanlar/fanlar_list.html', {
        'fanlar': fanlar,
        'purchased_fan_ids': purchased_fan_ids
    })