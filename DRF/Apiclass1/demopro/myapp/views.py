from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.http import JsonResponse
from django.views import View
from .models import Student   # 👈 only needed for StudentDetails

class GoodMorning(View):
    def get(self, request):
        return JsonResponse({"message": "Good Morning"})

class HelloWorld(View):
    def get(self, request):
        return JsonResponse({"message": "Hello World"})

class GoodEvening(View):
    def get(self, request):
        return JsonResponse({"message": "Good Evening"})

class UserDetails(View):
    def get(self, request):
        data = [
            {"name": "Arun", "age": 23, "place": "ekm"},
            {"name": "Amal", "age": 24, "place": "tvm"},
            {"name": "Anu",  "age": 25, "place": "ekm"},
        ]
        return JsonResponse(data, safe=False)   # 👈 safe=False allows list output

class StudentDetails(View):
    def get(self, request):
        students = Student.objects.all().values("rollnumber", "name", "age", "place", "marks")
        return JsonResponse(list(students), safe=False)


from django.http import JsonResponse
from django.views import View
from .models import Student

# class StudentList(View):
#     def get(self, request):
#         # fetch all students
#         s = Student.objects.all()
#
#         # print for debugging (optional)
#         print(s)
#         print(type(s)) #querie set of objectss
#
#         # return as JSON
#         return JsonResponse(list(s), safe=False)

#till this using Django not api

#
# from django.http import JsonResponse
# from django.views import View
# from myapp.models import Student
#
# class StudentList(View):
#     def get(self, request, *objects):
#         s = Student.objects.all()   # queryset of student objects
#         print(s)
#         print(type(s))
#
#         s = Student.objects.all().values()   # converts each object into dictionary
#         print(s)
#         print(type(s))   # queryset of student dictionaries
#
#         data = list(s)   # converts queryset into list format
#         print(data)
#         print(type(data))
#
#         return JsonResponse(data, safe=False)



# crud

# APIView for reading all student records
from django.http import JsonResponse
from django.views import View
from myapp.models import Student

# APIView for reading all student records
class StudentList(View):
    def get(self, request):
        s = list(Student.objects.all().values())  # queryset → list of dicts
        return JsonResponse(s, safe=False)


from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from json import loads
from myapp.models import Student

# APIView for creating a new student record

@method_decorator(csrf_exempt, name="dispatch")
class StudentCreate(View):
    def post(self, request):
        # convert JSON body into Python dict
        data = loads(request.body)

        r = data['rollnumber']
        n = data['name']
        a = data['age']
        p = data['place']
        m = data['marks']

        # create and save new student
        s = Student.objects.create(rollnumber=r, name=n, age=a, place=p, marks=m)
        s.save()

        return JsonResponse({"message": "Inserted Data success"})



class StudentDetail(View):
    def get(self, request, id):
        s = list(Student.objects.filter(id=id).values())  # queryset → list of dicts
        if s:   # if data exists
            return JsonResponse(s, safe=False)
        else:   # if no record found
            return JsonResponse({"message": "No Student Data"})


class StudentDelete(View):
    def delete(self, request, id):
        try:
            s = Student.objects.get(id=id)
            s.delete()
            return JsonResponse({"message": "Deleted Successfully"})
        except Student.DoesNotExist:
            return JsonResponse({"message": "No Student Found"})



import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from myapp.models import Student

@method_decorator(csrf_exempt, name="dispatch")
class StudentfullUpdate(View):
    def put(self, request, id):
        data = json.loads(request.body)

        try:
            s = Student.objects.get(id=id)
            s.rollnumber = data['rollnumber']
            s.name = data['name']
            s.age = data['age']
            s.place = data['place']
            s.marks = data['marks']
            s.save()
            return JsonResponse({'message': 'Updated Successfully'})
        except Student.DoesNotExist:
            return JsonResponse({'message': 'No Student Found'})



import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from myapp.models import Student

@method_decorator(csrf_exempt, name="dispatch")
class StudentpartialUpdate(View):
    def patch(self, request, id):
        data = json.loads(request.body)

        try:
            s = Student.objects.get(id=id)

            if 'rollnumber' in data:
                s.rollnumber = data['rollnumber']
            if 'name' in data:
                s.name = data['name']
            if 'age' in data:
                s.age = data['age']
            if 'place' in data:
                s.place = data['place']
            if 'marks' in data:
                s.marks = data['marks']

            s.save()
            return JsonResponse({'message': 'Updated Partially'})
        except Student.DoesNotExist:
            return JsonResponse({'message': 'No Student Found'})
