from django.http import HttpResponse   # correct import

# existing home view
def home(request):
    return HttpResponse("Welcome to Django Home")

# new index view
def index(request):
    return HttpResponse("Welcome to Django Index Page")
