from django.shortcuts import render

# Create your views here.
# request handlers

from django.http import HttpResponse
from django.template import loader
from .models import Employee

def index(request):
    myEmployees = Employee.objects.all().values()
    context = {
        'myEmployees': myEmployees
    }

    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))
    # return HttpResponse(output)