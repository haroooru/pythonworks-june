from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from movies.serializer import MovieSerializers
from movies.models import Movie
from rest_framework import status

# API VIEW FOR READING ALL RECORDS
class MovieListView(APIView):
    def get(self, request):
        data = Movie.objects.all()
        serializer_instance = MovieSerializers(data, many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)


# API VIEW FOR CREATING A NEW RECORD
class MovieCreate(APIView):
    def post(self, request):
        serializer_instance = MovieSerializers(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message": "Created successfully"},status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Invalid data", "errors": serializer_instance.errors},)


class MovieRetrieve(APIView):
    def get(self, request, id):
        movie = get_object_or_404(Movie, id=id)
        serializer_instance = MovieSerializers(movie)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def put(self, request, id):
        m = get_object_or_404(Movie, id=id)
        serializer_instance = MovieSerializers(m, data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message": "Updated successfully"},status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors)

    def patch(self, request, id):
        m = get_object_or_404(Movie, id=id)
        serializer_instance = MovieSerializers(m, data=request.data, partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message": "Updated successfully"},status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors)

    def delete(self, request, id):
        try:
            m = Movie.objects.get(id=id)
            m.delete()
            return Response({"message": "Deleted successfully"},status=status.HTTP_204_NO_CONTENT)
        except Movie.DoesNotExist:
            return Response({"message": "Movie not exist"},status=status.HTTP_404_NOT_FOUND)