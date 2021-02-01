from django.views.generic import CreateView
from .models import Contacts
from .forms import ContactForm
from .services import send
from .tasks import send_spam_email


class ContactView(CreateView):
    """Contact form representation"""

    model = Contacts
    form_class = ContactForm
    success_url = '/'
    template_name = 'mailer/contact.html'

    def form_valid(self, form):
        form.save()
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)
