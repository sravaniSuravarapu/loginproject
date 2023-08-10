from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import student
from .serializers import studentserializer
from rest_framework.renderers import JSONRenderer


# Create your views here.
def home(request):
    emp = student.objects.all()
    serializer = studentserializer(emp,many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,)
    


