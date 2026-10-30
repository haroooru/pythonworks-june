from django.contrib import admin
from django.urls import path
from employees import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i', views.EmployeeDetails.as_view()),
    path('j', views.EmployeeCreate.as_view()),
    path('k/<int:i>', views.EmployeeDelete.as_view()),
    path('l/<int:i>', views.EmployeeFullUpdate.as_view()),
    path('m/<int:i>', views.EmployeePartialUpdate.as_view()),
    path('n/<int:id>', views.EmployeeList.as_view()),

]
