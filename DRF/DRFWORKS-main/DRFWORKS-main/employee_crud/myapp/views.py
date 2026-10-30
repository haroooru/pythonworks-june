from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views import View
from rest_framework.utils.representation import serializer_repr

#create your views here.
from .models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import EmployeeSerializer
# API view for reading all employee records
class EmployeeList(APIView):

    def get(self, request):

        #qs=Employee.objects.all().values()
        qs = Employee.objects.all()

        #Employee.objects.all()
        #Employee.objects.get(condition)
        #Employee.objects.filter(condition)

           #Reads all employee records from Employee Table(qs)

        # e=list(qs)
        serializer_instance=EmployeeSerializer(qs,many=True)
           #EmployeeSerializer converts qs into python native types

           #qs contains more than one record so we use many=True

        return Response(data=serializer_instance.data)
           #sends python native data as json using Response class

# API view for creating a new employee record
from json import loads

# class EmployeeCreate(APIView):
#     def post(self,request):
#
#         #data=loads(request.body)  #converts json data into python native types
#         data=request.data  #python native type data or dictionary
#
#         # e=data['empid']
#         # n=data['name']
#         # a=data['age']
#         # p=data['place']
#         # g=data['gender']
#         # j=data['joining_date']
#         # s=data['salary']
#         # d=data['designation']
#
#         e=Employee.objects.create(**data)
#         e.save()
#
#         return Response({"message":"Inserted Data Successfully"})

#DESERIALIZATION
from rest_framework import status
class EmployeeCreate(APIView):
    def post(self,request):
        #View receives data as request.data(client side data -python native type)

        #Calls Serializer class for deserialization.here we pass request.data as
        #argument

        #after validations serializer saves data as model object inside db table

        serializer_instance=EmployeeSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)




# # API view for reading a specific employee record
#
# class EmployeeDetail(View):
#     def get(self,request,i):
#         e=list(Employee.objects.filter(id=i).values()) #json to dictionary
#         if e:
#             return Response(e,safe=False)
#         else:
#             return Response({'message':'No Student Data'})



class EmployeeDetail(APIView):
    def get(self,request,i):

        #Reads employee object from model
        #e=Employee.objects.get(id=i)
        e=get_object_or_404(Employee,id=i)  #show response

        #converts model object into python native using Employeeserializer
        serializer_instance=EmployeeSerializer(e)

        #sends the response as json us
        return Response(serializer_instance.data)




# # API view for deleting an employee record
#
# class EmployeeDelete(View):
#     def delete(self,request,i):
#         e=Employee.objects.get(id=i)
#         e.delete()
#         return JsonResponse({'message':'Deleted Successully'})
#

class EmployeeDelete(APIView):
    def delete(self,request,i):
        e=get_object_or_404(Employee,id=i)
        e.delete()
        return Response({'message':'deleted'})



# # API view for full update
# import json
#
# class Employeefullupdate(View):
#     def put(self,request,i):            #request.body - data coming from client app
#         data=json.loads(request.body)   #loads used to translate coming json data into
#                                         #python native/dictionary
#         print(data)
#         try:
#             e=Employee.objects.get(id=i)
#
#             e.empid=data['empid']
#             e.name=data['name']
#             e.age=data['age']
#             e.place=data['place']
#             e.gender=data['gender']
#             e.joining_date=data['joining_date']
#             e.salary=data['salary']
#             e.designation=data['designation']
#             e.save()
#
#             return JsonResponse({'message':'updated successfully'})
#         except:
#             return JsonResponse({'messsage':'No student data'})
#

class EmployeeFullUpdate(APIView):
    def put(self,request,i):

        e=Employee.objects.get(id=i)
        serializer_instance=EmployeeSerializer(e,request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()    #calls update() inside serializer class
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)



# # API view for partial update
#
# class Employeepartialupdate(View):
#     def patch(self,request,i):
#         data=json.loads(request.body)
#         try:
#             e = Employee.objects.get(id=i)
#             if 'empid' in data:
#                 e.empid=data['empid']
#             if 'name' in data:
#                 e.name=data['name']
#             if 'age' in data:
#                 e.age=data['age']
#             if 'place' in data:
#                 e.place=data['place']
#             if 'gender' in data:
#                 e.gender=data['gender']
#             if 'joining_date' in data:
#                 e.joining_date=data['joining_date']
#             if 'salary' in data:
#                 e.salary=data['salary']
#             if 'designation' in data:
#                 e.designation=data['designation']
#             e.save()
#
#             return JsonResponse({'message':'updated Partially'})
#         except:
#             return JsonResponse({'messsage':'No student data'})


class EmployeePartialUpdate(APIView):
    def patch(self,request,i):
        e = Employee.objects.get(id=i)
        serializer_instance = EmployeeSerializer(e, request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()  # calls update() inside serializer class
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)