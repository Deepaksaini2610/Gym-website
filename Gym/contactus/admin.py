from django.contrib import admin
from .models import Contact
from .models import mycontact
# Register your models here.
admin.site.register(Contact)
admin.site.register(mycontact)
