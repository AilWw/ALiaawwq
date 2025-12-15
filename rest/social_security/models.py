from django.db import models

class SocialSecurityEntry(models.Model):
    name = models.CharField(max_length=200)
    identity = models.CharField(max_length=200, unique=True)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
