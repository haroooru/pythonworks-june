from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import Employee
from myapp.serializers import EmployeeSerializer


#APIView for Reading all employee records
class EmployeeList(APIView):
    def get(self, request):
        qs = Employee.objects.all()
        #Reads all employee records from Employee Table(qs)
        serializer_instance = EmployeeSerializer(qs, many=True)
        #EmployeeSerializer converts qs into python native types
        #qs contains more than one record so we use many=True
        return Response(data=serializer_instance.data)
        #sends python native data as json using Response Class


# from json import loads

# # API View for creating a new Record
# class EmployeeCreate(APIView):
#     def post(self, request):
#         # data = loads(request.body)
#         data = request.data
#
#         # i = data['emp_id']
#         # n = data['name']
#         # a = data['age']
#         # g = data['gender']
#         # p = data['place']
#         # j = data['joining_date']
#         # s = data['salary']
#         # d = data['designation']
#
#         e = Employee.objects.create(**data)
#
#         e.save()
#
#         return Response({'message': 'created'})

# API View for creating a new Record
class EmployeeCreate(APIView):
    def post(self, request):
        # View receives data as request.data
        # Calls Serializer class for deserialization
        # Here we pass request.data as argument
        serializer_instance = EmployeeSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)


#APIView for reading a specific record
class EmployeeDetail(APIView):
    def get(self, request, i):
        # Reads employee object from model
        e = get_object_or_404(Employee, id=i)
        # Converts model object into python native
        # using EmployeeSerializer
        serializer_instance = EmployeeSerializer(e)
        # Sends the response as JSON
        return Response(serializer_instance.data)


#APIView for deleting a specific record
class EmployeeDelete(APIView):
    def delete(self, request, i):
        e = get_object_or_404(Employee, id=i)
        e.delete()
        return Response({"message": "deleted"})


#APIView for updating an existing record
class EmployeeUpdate(APIView):
    def patch(self, request, i):
        e = get_object_or_404(Employee, id=i)
        serializer_instance = EmployeeSerializer(
            e, data=request.data, partial=True
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)


#APIView for partially updating a record
class EmployeePartialUpdate(APIView):
    def patch(self, request, i):
        e = get_object_or_404(Employee, id=i)
        serializer_instance = EmployeeSerializer(
            e, data=request.data, partial=True
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)
