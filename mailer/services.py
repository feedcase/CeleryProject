from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Как и обещали',
        'Будет много спама',
        '1502seva@gmail.com',
        [user_email],
        fail_silently=False,
    )
