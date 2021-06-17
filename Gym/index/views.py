from django.shortcuts import render
from .models import  about
# Create your views here.
def pyare(request):
    aboutdata = about.objects.all()[0]
    data = {
        'deepak':aboutdata
    }
    return  render(request,'index/index.html',data)