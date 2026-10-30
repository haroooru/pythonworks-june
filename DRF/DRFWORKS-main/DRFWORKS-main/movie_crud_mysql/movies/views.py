from django.shortcuts import render, get_object_or_404

# Create your views here.

#APIView for reading all movie records
from rest_framework.views import APIView
from .models import Movies
from .serializers import MovieSerializer
from rest_framework.response import Response
# class MovieList(APIView):
#     def get(self,request):
#
#         #qs
#         m=Movies.objects.all()
#
#         #serializer instance
#         serializer_instance=MovieSerializer(m,many=True)
#
#         #Response
#         return Response(serializer_instance.data)


#APIView for creating a new record

#request.data
#serializer_instance
#validation
#create() in serializer class for saving
#Response

# class MovieCreate(APIView):
#     def post(self,request):
#
#         form_data=request.data
#         serializer_instance = MovieSerializer(data=form_data)
#
#         if serializer_instance.is_valid():
#             #data after validation
#             # cleaned_data=serializer_instance.validated_data
#             # print(cleaned_data)
#             # title=cleaned_data['title']
#
#             serializer_instance.save()
#             return Response(serializer_instance.data)
#         else:
#             return Response(serializer_instance.errors)

#Non primary key based in one class(list and create)
from rest_framework import status
class MovieListCreate(APIView):
    def get(self,request):

        #qs
        m=Movies.objects.all()

        #serializer instance
        serializer_instance=MovieSerializer(m,many=True)

        #Response
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def post(self,request):

        form_data=request.data
        serializer_instance = MovieSerializer(data=form_data)

        if serializer_instance.is_valid():
            #data after validation
            # cleaned_data=serializer_instance.validated_data
            # print(cleaned_data)
            # title=cleaned_data['title']

            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)




class MovieRetrieveUpdateDelete(APIView):
    # APIView for reading a specific record
    #modelobject
    #serializer
    #Response
    def get(self,request,i):
        m=get_object_or_404(Movies,id=i)
        serializer_instance=MovieSerializer(m)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    # APIView for updating all records
    #data
    #serializer_instance(instance,data)
    #validation
    #update() in serializer class for saving
    #Response
    def put(self,request,i):
        form_data=request.data
        m=Movies.objects.get(id=i)  #reads movie instance
        serializer_instance = MovieSerializer(m,data=form_data)

        if serializer_instance.is_valid():

            #data after validation
            # cleaned_data=serializer_instance.validated_data
            # print(cleaned_data)
            # title=cleaned_data['title']

            serializer_instance.save()
            return Response(serializer_instance.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_204_NO_CONTENT)


    def patch(self,request,i):
        form_data=request.data
        m=Movies.objects.get(id=i)
        serializer_instance = MovieSerializer(m,data=form_data,partial=True)

        if serializer_instance.is_valid():

            #data after validation
            # cleaned_data=serializer_instance.validated_data
            # print(cleaned_data)
            # title=cleaned_data['title']

            serializer_instance.save()
            return Response(serializer_instance.data,status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_204_NO_CONTENT)

    # APIView for deleting a specific record

    #modelobject
    #delete()

    def delete(self,request,i):
        m=get_object_or_404(Movies,id=i)
        m.delete()
        return Response({'Message':'Movie Deleted'},status=status.HTTP_204_NO_CONTENT)


    def validate(self,data):
        if data['age']<=0:
            raise
