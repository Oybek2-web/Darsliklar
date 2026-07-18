from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Fanlar, SotibOlinganFan
from .forms import FanlarForms
from darsliklar.models import Darsliklar


def fanlar_list(request):
    fanlar = Fanlar.objects.all()
    purchased_fan_ids = []

    # Agar foydalanuvchi tizimga kirgan bo'lsa, uning sotib olgan fanlari ID larini olamiz
    if request.user.is_authenticated:
        purchased_fan_ids = list(SotibOlinganFan.objects.filter(
            user=request.user, tolov_holati=True
        ).values_list('fan_id', flat=True))

    return render(request, 'fanlar/fanlar_list.html', {
        'fanlar': fanlar,
        'purchased_fan_ids': purchased_fan_ids
    })


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
    """Fanni sotib olish logikasi (Hozircha test uchun avtomatik tasdiqlaydi)"""
    fan = get_object_or_404(Fanlar, id=id)

    # Agar fan bepul bo'lsa, to'g'ridan-to'g'ri darslikka yo'naltiramiz
    if not fan.price or fan.price == 0:
        return redirect('fanlar:darsliklar_kirish', id=fan.id)

    # Allaqachon sotib olganini tekshirish
    already_purchased = SotibOlinganFan.objects.filter(user=request.user, fan=fan, tolov_holati=True).exists()

    if already_purchased:
        messages.info(request, "Siz bu fanni allaqachon sotib olgansiz.")
        return redirect('fanlar:darsliklar_kirish', id=fan.id)

    # YANGI YOZUV QO'SHISH (Haqiqiy loyihada bu yerda Click/Payme API ishlaydi)
    SotibOlinganFan.objects.create(user=request.user, fan=fan, tolov_holati=True)
    messages.success(request, f"'{fan.title}' fani muvaffaqiyatli sotib olindi!")

    return redirect('fanlar:darsliklar_kirish', id=fan.id)


@login_required
def darsliklar_kirish(request, id):
    """Fanni ochish va sotib olinganini tekshirish"""
    fan = get_object_or_404(Fanlar, id=id)

    is_purchased = SotibOlinganFan.objects.filter(user=request.user, fan=fan, tolov_holati=True).exists()
    is_free = not fan.price or fan.price == 0

    # Agar pullik bo'lsa va sotib olinmagan bo'lsa, ruxsat bermaymiz
    if not is_free and not is_purchased:
        messages.error(request, "Ushbu fanni ko'rish uchun avval uni sotib olishingiz kerak.")
        return redirect('fanlar:fanlar_list')

    darsliklar = Darsliklar.objects.filter(fan=fan)
    return render(request, 'darsliklar/darsliklar_kirish.html', {
        'fan': fan,
        'darsliklar': darsliklar,
        'is_purchased': True
    })