from pyexpat import model
from re import template
from django.shortcuts import render
from .models import Task
from django.views.generic import ListView 

class TaskListView(ListView):
    model = Task
    context_object_name = 'taskobj'