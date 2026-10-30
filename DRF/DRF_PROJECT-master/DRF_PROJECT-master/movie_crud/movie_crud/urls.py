from django.contrib import admin
from django.urls import path,include
from movies import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('movies',views.MovieViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('moviesv', views.MovieListView.as_view()),
    # path('moviesc', views.MovieCreate.as_view()),
    # path('movies/<int:id>', views.MovieRetrieve.as_view()),
    # path('movies/<int:pk>', views.MovieRetrieveUpdateDestroy.as_view()),
    # path('movies2', views.MovieListCreate.as_view()),
    # path('movies21', views.MovieRetrieveUpdateDestroy.as_view()),
    path('', include(router.urls)),
    path('Search', views.SearchMovie.as_view()),
    path('Searchgene', views.SearchMovies.as_view()),
    path('register', views.RegisterApiView.as_view()),

]
