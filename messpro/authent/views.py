from django.shortcuts import render
from django.http import HttpResponse
import io;
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import studentgrp
from.serializers import studentserialia
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
# Create your views here.
def h(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            stu = studentgrp.objects.get(id = id)
            serializer = studentserialia(stu)
            print(serializer)
            json_data = JSONRenderer().render(serializer.data)
            print(json_data)
            return HttpResponse(json_data,content_type = 'appliction/json')
        stu = studentgrp.objects.all()
        serializer = studentserialia(stu,many = True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type ='application/json')
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = studentgrp.objects.get(id = id)
        stu.delete()
        return HttpResponse("data is succesfully deleted")
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        stu = studentgrp.objects.get(id = id)
        serializer = studentserialia(stu,data = python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {
                'msg': 'created',
            }
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application\json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type= 'application\json')
    return HttpResponse('data is saved successfully ')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = studentserialia(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {
                'msg': 'created',
            }
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type = 'application\json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type= 'application\json')
    return HttpResponse('data is saved successfully ')
   
   
    
    
        
         
