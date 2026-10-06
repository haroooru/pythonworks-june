from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.views import View
from .models import Employee

class EmployeeList(View):

    def get(self, request):
        employees = Employee.objects.all()

        data = []

        for employee in employees:
            data.append({
                'empid': employee.empid,
                'name': employee.name,
                'age': employee.age,
                'place': employee.place,
                'gender': employee.gender,
                'joining_date': employee.joining_date,
                'salary': employee.salary,
                'designation': employee.designation
            })

        return JsonResponse(data, safe=False)


class EmployeeCreate(View):

    def post(self, request):

        data = json.loads(request.body)

        employee = Employee.objects.create(
            empid=data['empid'],
            name=data['name'],
            age=data['age'],
            place=data['place'],
            gender=data['gender'],
            joining_date=data['joining_date'],
            salary=data['salary'],
            designation=data['designation']
        )

        return JsonResponse({
            'message': 'Employee created successfully',
            'empid': employee.empid
        })


class EmployeeRetrieve(View):

    def get(self, request, id):

        employee = Employee.objects.get(empid=id)

        data = {
            'empid': employee.empid,
            'name': employee.name,
            'age': employee.age,
            'place': employee.place,
            'gender': employee.gender,
            'joining_date': employee.joining_date,
            'salary': employee.salary,
            'designation': employee.designation
        }

        return JsonResponse(data)

class EmployeeFullUpdate(View):

    def put(self, request, id):

        data = json.loads(request.body)

        employee = Employee.objects.get(empid=id)

        employee.name = data['name']
        employee.age = data['age']
        employee.place = data['place']
        employee.gender = data['gender']
        employee.joining_date = data['joining_date']
        employee.salary = data['salary']
        employee.designation = data['designation']

        employee.save()

        return JsonResponse({
            'message': 'Employee updated successfully'
        })


class EmployeePartialUpdate(View):

    def patch(self, request, id):

        data = json.loads(request.body)

        employee = Employee.objects.get(empid=id)

        if 'name' in data:
            employee.name = data['name']

        if 'age' in data:
            employee.age = data['age']

        if 'place' in data:
            employee.place = data['place']

        if 'gender' in data:
            employee.gender = data['gender']

        if 'joining_date' in data:
            employee.joining_date = data['joining_date']

        if 'salary' in data:
            employee.salary = data['salary']

        if 'designation' in data:
            employee.designation = data['designation']

        employee.save()

        return JsonResponse({
            'message': 'Employee partially updated successfully'
        })

class EmployeeDelete(View):

    def delete(self, request, id):

        employee = Employee.objects.get(empid=id)

        employee.delete()

        return JsonResponse({
            'message': 'Employee deleted successfully'
        })