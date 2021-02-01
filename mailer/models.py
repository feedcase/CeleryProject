from django.db import models


class Contacts(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'EmailSubscribers'
