from django.shortcuts import render

# Create your views here.
# request handlers

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Employee
from django.urls import reverse

def index(request): # ceo cfo cob coo
    management = Employee.objects.filter(title__in=["CEO","CFO","COB","COO"])
    employees = Employee.objects.all().values().exclude(title__in=["CEO","CFO","COB","COO"])
    context = {
        "management": management,
        'employees': employees,
        "Title": "Employees"
    }

    template = loader.get_template('employee/index.html')
    return HttpResponse(template.render(context, request))

def addEmployee(request):
    template = loader.get_template('employee/addEmployee.html')
    return HttpResponse(template.render({"Title": "Add employees"}, request))

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

def updateEmployee(request, id):
    employeeToUpdate = Employee.objects.get(id=id)
    context = {
        'empl': employeeToUpdate,
        'Title': "Update"
    }

    template = loader.get_template('employee/updateEmployee.html')
    return HttpResponse(template.render(context, request))

def updateResult(request, id):
    nameReceived = request.POST["name"]
    titleReceived = request.POST["title"]

    employeeToUpdate = Employee.objects.get(id=id)

    employeeToUpdate.name = nameReceived
    employeeToUpdate.title = titleReceived

    employeeToUpdate.save()

    return HttpResponseRedirect(reverse('index'))