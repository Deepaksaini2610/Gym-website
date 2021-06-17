from django.db import models

# Create your models here.
class Contact(models.Model):
    first_name = models.CharField(max_length=50,default=False)
    last_name = models.CharField(max_length=50,default=False)
    age = models.IntegerField(default=False)
    n = models.CharField(max_length=12,default=False)
    def __str__(self):
        return f"{self.first_name} "
class mycontact(models.Model):
    email = models.TextField(max_length= 50,default=False)
    address = models.TextField(max_length=100,default=False)
    number = models.CharField(max_length=12,default=False)
    def __str__(self):
        return self.address