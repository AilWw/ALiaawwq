from django.db import models

class FakEntry(models.Model):
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=200, unique=True)
    payment_status = models.CharField(max_length=100)
    whatsapp_name = models.CharField(max_length=200, blank=True, null=True)
    entry_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
