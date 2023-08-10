from rest_framework import serializers
from .models import studentgrp

class studentserialia(serializers.Serializer):
    fname = serializers.CharField(max_length=50)
    sname = serializers.CharField(max_length=50)
    ph_no = serializers.IntegerField(default=0)
    def create(self,validate_data):
        return studentgrp.objects.create(**validate_data)
    def update(self, instance, validated_data):
        instance.fname = validated_data.get('fname',instance.fname)
        print(instance.fname)
        instance.sname = validated_data.get('sname',instance.sname)
        instance.ph_no = validated_data.get('ph_no',instance.ph_no)
        instance.save()
        return instance