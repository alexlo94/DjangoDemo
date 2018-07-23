# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

#define models here
#defining 2 models, employee and position with a many-to-one relationship (e.g. many employees can have the same position but not vice versa)

#define the position model
class Position(models.Model):
    name = models.CharField(max_length = 100)
    salary = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return "%s" % (self.name)

    pass

#define the employee model
class Employee(models.Model):
    name = models.CharField(max_length = 50)
    age = models.IntegerField()
    hired = models.DateField(blank = True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % (self.name)
    

