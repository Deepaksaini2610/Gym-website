from django.db import models

# Create your models here.
class about(models.Model):
    title = models.TextField(max_length=50,blank=False)
    description = models.TextField(max_length=150 ,blank= False)
    def __str__(self):
        return self.title
