
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from myapp.models import Student
import json
from json import loads


# Basic views

class GoodMorning(View):
    def get(self, request):
        data = {"Message": "Good Morning"}
        return JsonResponse(data)


class HelloWorld(View):
    def get(self, request):
        data = {"Message": "Hello World"}
        return JsonResponse(data)


class GoodEvening(View):
    def get(self, request):
        data = {"Message": "Good Evening"}
        return JsonResponse(data)


# User details

class Userdetails(View):
    def get(self, request):
        data = [
            {'name': 'Arun', 'age': 23, 'place': 'ekm'},
            {'name': 'Amal', 'age': 24, 'place': 'tvm'},
            {'name': 'Anu', 'age': 25, 'place': 'ekm'}
        ]
        return JsonResponse(data, safe=False)


# CRUD

# API view for reading all student records
class StudentList(View):
    def get(self, request):
        s = list(Student.objects.all().values())
        return JsonResponse(s, safe=False)


# API view for creating a new student record
@method_decorator(csrf_exempt, name="dispatch")
class StudentCreate(View):
    def post(self, request):
        data = loads(request.body)

        r = data['roll_no']
        n = data['name']
        a = data['age']
        p = data['place']
        m = data['marks']

        s = Student.objects.create(
            roll_no=r,
            name=n,
            age=a,
            place=p,
            marks=m
        )
        s.save()

        return JsonResponse({"message": "Inserted Data successfully"})


# API view for reading a specific record
class StudentDetail(View):
    def get(self, request, id):
        s = list(Student.objects.filter(id=id).values())

        if s:
            return JsonResponse(s, safe=False)
        else:
            return JsonResponse({"message": "No Student Data"})


@method_decorator(csrf_exempt, name="dispatch")
class StudentDelete(View):
    def delete(self, request, id):
        s = Student.objects.get(id=id)
        s.delete()
        return JsonResponse({"Message": "Deleted Successfully"})


@method_decorator(csrf_exempt, name="dispatch")
class Studentfullupdate(View):
    def put(self, request, id):
        data = json.loads(request.body)
        print(data)

        try:
            s = Student.objects.get(id=id)

            s.roll_no = data['roll_no']
            s.name = data['name']
            s.age = data['age']
            s.place = data['place']
            s.marks = data['marks']
            s.save()

            return JsonResponse({'message': 'updated successfully'})
        except:
            return JsonResponse({'message': "No student Data"})


@method_decorator(csrf_exempt, name="dispatch")
class Studentpartialupdate(View):
    def patch(self, request, id):
        data = json.loads(request.body)

        try:
            s = Student.objects.get(id=id)

            if 'roll_no' in data:
                s.roll_no = data['roll_no']
            if 'name' in data:
                s.name = data['name']
            if 'age' in data:
                s.age = data['age']
            if 'place' in data:
                s.place = data['place']
            if 'marks' in data:
                s.marks = data['marks']

            s.save()
            return JsonResponse({"message": "Updated Partially"})

        except:
            return JsonResponse({"message": "No student data"})
