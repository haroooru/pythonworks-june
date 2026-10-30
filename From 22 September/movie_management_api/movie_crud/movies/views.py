from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from movies.models import Movie
from movies.serializers import MovieSerializer


# 1. Display all movies
class MovieList(APIView):
    def get(self, request):
        m = Movie.objects.all()
        serializer_instance = MovieSerializer(m, many=True)
        return Response(serializer_instance.data)


# 2. Create a movie
class MovieCreate(APIView):
    def post(self, request):
        form_data = request.data
        serializer_instance = MovieSerializer(data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)


# 3. Retrieve, update and delete a movie
class MovieRetrieveUpdateDelete(APIView):

    def get(self, request, id):
        m = get_object_or_404(Movie, id=id)
        serializer_instance = MovieSerializer(m)
        return Response(serializer_instance.data)

    def put(self, request, id):
        form_data = request.data
        m = get_object_or_404(Movie, id=id)
        serializer_instance = MovieSerializer(m, data=form_data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

    def patch(self, request, id):
        form_data = request.data
        m = get_object_or_404(Movie, id=id)
        serializer_instance = MovieSerializer(
            m, data=form_data, partial=True
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

    def delete(self, request, id):
        m = get_object_or_404(Movie, id=id)
        m.delete()
        return Response({"Message": "Movie is Deleted"})


# 4. ViewSet approach (alternative)
class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# 5. Search movies by title
class SearchAPIView(APIView):
    def get(self, request):
        data = request.query_params.get('search')
        m = Movie.objects.filter(title=data)
        serializer_instance = MovieSerializer(m, many=True)
        return Response(
            serializer_instance.data,
            status=status.HTTP_200_OK
        )

# --------------------------------------------------
# Alternative approach: Generics
# Keeping this code commented out for reference
# --------------------------------------------------

# from rest_framework import generics
#
# class MovieListCreate(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
# class MovieRetrieveUpdateDelete(
#     generics.RetrieveUpdateDestroyAPIView
# ):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


# --------------------------------------------------
# Alternative approach: Mixins
# Keeping this code commented out for reference
# --------------------------------------------------

# from rest_framework import mixins, generics
#
# class MovieListCreate(
#     mixins.ListCreateModelMixin,
#     generics.GenericAPIView
# ):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
# class MovieRetrieveUpdateDelete(
#     mixins.RetrieveUpdateDestroyModelMixin,
#     generics.GenericAPIView
# ):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
#     def get(self, request, pk):
#         return self.retrieve(request, pk)
#
#     def put(self, request, pk):
#         return self.update(request, pk)
#
#     def patch(self, request, pk):
#         return self.partial_update(request, pk)
#
#     def delete(self, request, pk):
#         return self.destroy(request, pk)
