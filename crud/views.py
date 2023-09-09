from .models import *
from django.http import JsonResponse
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render


@api_view(['GET', 'POST'])
def phones_list(request, format = None):


    #get all the phones 
    #serialize them
    #return json
    if request.method == 'GET':
       phones = Phones.objects.all()
       serializer = PhoneSerializer(phones, many = True)
       return Response(serializer.data, status=status.HTTP_200_OK)
      
    
    if request.method == 'POST':
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])       
def details(request, pk, format = None):

    try:
        phone = Phones.objects.get(id=pk)
    except Phones.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PhoneSerializer(phone)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PhoneSerializer(phone, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    elif request.method == 'DELETE':
        phone.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    

@api_view(['GET','POST'])
def student_list(request, format = None):
    if request.method == 'GET':
       students = Student.objects.all()
       serializer = StudentSerializer(students, many=True)
       return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET','PUT','DELETE'])
def student_details(request,pk, format = None):
    try:
        students = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(students)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(students, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

