from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy


def login_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:

            next_url = request.get_full_path()
            return redirect(f"{reverse_lazy('accounts:login')}?next={next_url}")

    return wrapper


from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings


def send_reset_password_email(email, code):
    html_message = render_to_string(
        'registration/password_reset_email.html', {'code': code})
    plain_message = f"Your OTP code is: {code}"

    msg = EmailMultiAlternatives(
        subject="Password Reset OTP",
        body=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        to=[email],
    )

    msg.attach_alternative(html_message, "text/html")
    msg.send(fail_silently=False)
