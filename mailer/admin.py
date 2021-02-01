from django.contrib import admin
from .models import Contacts


@admin.register(Contacts)
class MailerAdmin(admin.ModelAdmin):
    list_display = ['name', ]
