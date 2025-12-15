from django.db import models

class ResidentEntry(models.Model):
    name = models.CharField(max_length=200)
    residency_number = models.CharField(max_length=200, unique=True)
    company = models.CharField(max_length=200)
    expiry_date = models.DateField()

    def __str__(self):
        return self.name
