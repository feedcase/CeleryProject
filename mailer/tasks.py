from django.core.mail import send_mail
from mailer.celery import app
from .services import send
from .models import Contacts


@app.task
def send_spam_email(user_email):
    send(user_email)
