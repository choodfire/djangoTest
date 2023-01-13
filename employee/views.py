from django.shortcuts import render

# Create your views here.
# request handlers

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Employee
from django.urls import reverse

def index(request):
    myEmployees = Employee.objects.all().values()
    context = {
        'myEmployees': myEmployees
    }

    template = loader.get_template('index.html')
    return HttpResponse(template.render(context, request))

def addEmployee(request):
    template = loader.get_template('addEmployee.html')
    return HttpResponse(template.render({}, request))

def addResult(request):
    nameReceived = request.POST["name"]
    titleReceived = request.POST["title"]
    newEmployee = Employee(name=nameReceived, title=titleReceived)

    newEmployee.save()

    return HttpResponseRedirect(reverse('index'))

def deleteEmployee(request, id):
    employeeToDelete = Employee.objects.get(id=id)
    employeeToDelete.delete()

    return HttpResponseRedirect(reverse('index'))

