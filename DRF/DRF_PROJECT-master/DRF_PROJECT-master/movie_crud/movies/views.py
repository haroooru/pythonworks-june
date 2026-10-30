from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.shortcuts import get_object_or_404
from movies.serializer import MovieSerializers, UserSerializer
from movies.models import Movie
from django.db.models import Q


# # API VIEW FOR READING ALL RECORDS
# class MovieListView(APIView):
#     def get(self, request):
#         data = Movie.objects.all()
#         serializer_instance = MovieSerializers(data, many=True)
#         return Response(serializer_instance.data, status=status.HTTP_200_OK)
#
#
# # API VIEW FOR CREATING A NEW RECORD
# class MovieCreate(APIView):
#     def post(self, request):
#         serializer_instance = MovieSerializers(data=request.data)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response({"message": "Created successfully"}, status=status.HTTP_201_CREATED)
#         else:
#             return Response(
#                 {"message": "Invalid data"},status=status.HTTP_400_BAD_REQUEST)
#
#
# # API VIEW FOR RETRIEVE, UPDATE AND DELETE
# class MovieRetrieve(APIView):
#     def get(self, request, id):
#         movie = get_object_or_404(Movie, id=id)
#         serializer_instance = MovieSerializers(movie)
#         return Response(serializer_instance.data, status=status.HTTP_200_OK)
#
#     def put(self, request, id):
#         m = get_object_or_404(Movie, id=id)
#         serializer_instance = MovieSerializers(m, data=request.data)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response({"message": "Updated successfully"}, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def patch(self, request, id):
#         m = get_object_or_404(Movie, id=id)
#         serializer_instance = MovieSerializers(m, data=request.data, partial=True)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response({"message": "Updated successfully"}, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         try:
#             m = Movie.objects.get(id=id)
#             m.delete()
#             return Response({"message": "Deleted successfully"}, status=status.HTTP_200_OK)
#         except Movie.DoesNotExist:
#             return Response({"message": "Movie not exist"}, status=status.HTTP_404_NOT_FOUND)




# #       MIXINS
#
# from rest_framework import mixins,generics
# class MovieListCreate(mixins.ListModelMixin,
#                       mixins.CreateModelMixin,
#                       generics.GenericAPIView):
#
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializers
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class MovieRetrieveUpdateDestroy(mixins.RetrieveModelMixin,
#                                  mixins.UpdateModelMixin,
#                                  mixins.DestroyModelMixin,
#                                  generics.GenericAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializers
#     def get(self, request,pk):
#         return self.retrieve(request,pk)
#     def put(self, request,pk):
#         return self.update(request,pk)
#     def patch(self,request,pk):
#         return self.partial_update(request,pk)
#     def delete(self,request,pk):
#         return self.destroy(request,pk)


# # GENERICS
#
# from rest_framework import generics
# class MovieListCreate(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializers
#
# class MovieRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializers

# Viewsets

from rest_framework import viewsets
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers



class SearchMovie(APIView):
    def get(self,request):
        data=self.request.query_params.get('search')
        m=Movie.objects.filter(Q(title__icontains=data)|
                               Q(director__icontains=data))
        if not m.exists():
            return Response({"NOT FOUND"},status=status.HTTP_200_OK)

        serializer_instance=MovieSerializers(m,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

from rest_framework.filters import SearchFilter
class SearchMovies(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializers
    filter_backends = [SearchFilter]
    search_fields = ['title','director','language']

class RegisterApiView(APIView):
    def get(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response({"message":"User created successfully."},status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"Something went wrong."},status=status.HTTP_400_BAD_REQUEST)