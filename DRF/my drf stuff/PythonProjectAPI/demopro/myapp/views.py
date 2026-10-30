from django.http import JsonResponse
from django.views import View


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


class UserDetails(View):

    data = [
        {'name': 'Arun', 'age': 23, 'place': 'ekm'},
        {'name': 'Amal', 'age': 24, 'place': 'tvm'},
        {'name': 'Anu', 'age': 25, 'place': 'ekm'}
    ]

    def get(self, request):
        return JsonResponse(self.data, safe=False)