from django.shortcuts import render
from django.views import View


def home(request):
    return render(request, 'home.html')


class Add(View):
    def get(self, request):
        return render(request, 'add.html')

    def post(self, request):
        n1 = int(request.POST['number1'])
        n2 = int(request.POST['number2'])

        s = n1 + n2

        return render(request, 'add.html', {'sum': s})