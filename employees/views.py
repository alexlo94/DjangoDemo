from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Position

#view to return on ~/employees/
def index(request):
    return render(request, 'employees/index.html')

#view to return on ~/employees/employeelist
def employeelist(request):
    employees = Employee.objects.all() #gather up all the employee objects
    context = {
        'employees' : employees
    }
    #render the employeelist template with the data from context
    return render(request, 'employees/employeelist.html', context)

#view to return on ~/employees/positionlist
def positionlist(request):
    positions = Position.objects.all() #gather up all the position objects
    context = {
        'positions' : positions
    }
    return render(request, 'employees/positionlist.html', context)
