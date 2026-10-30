from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from employees.serializers import EmployeeSerializers
from employees.models import Employee

class EmployeeDetails(APIView):
    def get(self, request):
        data = Employee.objects.all()

        # Reads all employee records from the Employee Table
        serializer = EmployeeSerializers(data, many=True)
        # EmployeeSerializer convert the qs into python native types
        # qs contains more than one record so we use many=True
        return Response(data=serializer.data)
# API view for creating records

class EmployeeCreate(APIView):
    def post(self, request):
        # data=request.data
        # eid=data["employee_id"]
        # name=data["employee_name"]
        # age=data["employee_age"]
        # gender=data["employee_gender"]
        # salary=data["employee_salary"]
        # joining_date=data["employee_joining_date"]
        # designation=data["employee_designation"]
        # e = Employee.objects.create(
        #     employee_id=eid,
        #     employee_name=name,
        #     employee_age=age,
        #     employee_gender=gender,
        #     employee_salary=salary,
        #     employee_joining_date=joining_date,
        #     employee_designation=designation,
        # )
        # e.save()
        # return Response({"message": "Inserted data successfully"})

        # Views receives data as request.data(client side data python native data)
        # Calls Serializer class for deserialization.Here we pass request.data as argument
        # after validation serializer saves data as model object inside db table

        serializer_instance = EmployeeSerializers(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message": "Created successfully"})
        else:
            return Response({"message": "Invalid data"})


class EmployeeDelete(APIView):
    def delete(self, request,i):
        try:
            e=Employee.objects.get(id=i)
            e.delete()
            return Response({"message": "Deleted successfully"})
        except Employee.DoesNotExist:
            return Response({"message": "Employee not exist"})


class EmployeeFullUpdate(APIView):
    def put(self, request,i):
        # data=request.data
        # try:
        #     e=Employee.objects.get(id=i)
        #     e.employee_id=data["employee_id"]
        #     e.employee_name=data["employee_name"]
        #     e.employee_age=data["employee_age"]
        #     e.employee_gender=data["employee_gender"]
        #     e.employee_salary=data["employee_salary"]
        #     e.employee_joining_date=data["employee_joining_date"]
        #     e.employee_designation=data["employee_designation"]
        #     e.save()
        #     return Response({"message": "Updated successfully"})
        # except Employee.DoesNotExist:
        #     return Response({"message": "Employee not exist"})
        e=get_object_or_404(Employee,id=i)
        serializer_instance = EmployeeSerializers(e,request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message": "Updated successfully"})
        else:
            return Response(serializer_instance.errors)


class EmployeePartialUpdate(APIView):
    def patch(self, request,i):
        # data=request.data
        # try:
        #     e=Employee.objects.get(id=i)
        #     if "employee_id" in data:
        #         e.employee_id=data["employee_id"]
        #     if "employee_name" in data:
        #         e.employee_name=data["employee_name"]
        #     if "employee_age" in data:
        #         e.employee_age=data["employee_age"]
        #     if "employee_gender" in data:
        #         e.employee_gender=data["employee_gender"]
        #     if "employee_salary" in data:
        #         e.employee_salary=data["employee_salary"]
        #     if "employee_joining_date" in data:
        #         e.employee_joining_date=data["employee_joining_date"]
        #     if "employee_designation" in data:
        #         e.employee_designation=data["employee_designation"]
        #     e.save()
        #     return Response({"message": "Updated successfully"})
        # except Employee.DoesNotExist:
        #     return Response({"message": "Employee not exist"})
        e=get_object_or_404(Employee,id=i)
        serializer_instance = EmployeeSerializers(e,request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message": "Updated successfully"})
        else:
            return Response(serializer_instance.errors)

class EmployeeList(APIView):
    def get(self, request,id):
        employee=Employee.objects.get(id=id)
        # employee=get_object_404(Employee,employee_id=id)
        if employee:
            serializer_instance=EmployeeSerializers(employee)
            return Response(serializer_instance.data)
        else:
            return Response({"message": "Employee not exist"})