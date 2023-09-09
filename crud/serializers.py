from rest_framework import serializers
from .models import *

class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = ['id','name','price']

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'f_name','l_name','sex','dob']