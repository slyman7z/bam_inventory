from django.db import models



# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone1 = models.CharField(max_length=13)
    phone2 = models.CharField(max_length=13, blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, default='Nigeria')

    def __str__(self):
        return self.name
