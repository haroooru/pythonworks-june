from django.contrib import admin
from django.urls import path
from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('moviesv', views.MovieListView.as_view()),
    path('moviesc', views.MovieCreate.as_view()),
    path('movies/<int:id>', views.MovieRetrieve.as_view()),
]
