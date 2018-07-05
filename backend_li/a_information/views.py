from django.shortcuts import render, HttpResponse


# Create your views here.


# .表示当前包下的models

from .models import StudentModel
from django.views.generic import View

class Student(View):

    def get(self, request):
        StudentModel.objects.create(name='水痕', age= 20)
        return HttpResponse('hello word')