from django.shortcuts import render
from django.http import  HttpResponse
from .models import Contact
from  .models import mycontact
#Create your views here.
def hello(request):
    # contactdata = Contact.objects.all()
    datacontact = mycontact.objects.all()[0]
    data = {
        'mydata': datacontact
    }
    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        age = request.POST.get('lage')
        n = request.POST.get("lnum")
        contactform = Contact(first_name = first_name,last_name = last_name,age = age,n = n)
        contactform.save()

    return render(request,"contact/contact.html",data)