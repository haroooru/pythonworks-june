from django.shortcuts import render

# Create your views here.
#
# from rest_framework.views import APIView
# from rest_framework.response import Response
#
# from movies.models import Movie
# from movies.serializers import MovieSerializer
#
#
# # API View for reading all movie records
# class MovieList(APIView):
#
#     def get(self, request):
#
#         # Queryset
#         m = Movie.objects.all()
#
#         # Serializer instance
#         serializer_instance = MovieSerializer(m, many=True)
#
#         # Response
#         return Response(serializer_instance.data)

from django.shortcuts import render

from rest_framework.views import APIView

from movies.models import Movie

from movies.serializers import MovieSerializer

from rest_framework.response import Response

from django.shortcuts import get_object_or_404


# GET, POST, PUT, PATCH, Delete


# API View for reading all movie records

class MovieListCreate(APIView):

    def get(self, request):

        # qs
        m = Movie.objects.all()

        # serializer instance
        serializer_instance = MovieSerializer(m, many=True)

        # Responses
        return Response(serializer_instance.data)


    # API View for creating a new record

    def post(self, request):

        form_data = request.data

        serializer_instance = MovieSerializer(data=form_data)

        if serializer_instance.is_valid():

            # Data After validation
            # cleaned_data = serializer_instance.validated_data
            # title = cleaned_data['title']

            serializer_instance.save()

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)


# API View for reading, updating and deleting a specific record

class MovieRetrieveUpdateDelete(APIView):

    # APIView for reading a specific record

    def get(self, request, id):

        # model object
        m = get_object_or_404(Movie, id=id)

        # serializer
        serializer_instance = MovieSerializer(m)

        # Response
        return Response(serializer_instance.data)


    # API View for updating a specific record

    def put(self, request, id):

        form_data = request.data

        m = Movie.objects.get(id=id)

        serializer_instance = MovieSerializer(m, data=form_data)

        if serializer_instance.is_valid():

            # Data After validation
            # cleaned_data = serializer_instance.validated_data
            # title = cleaned_data['title']

            serializer_instance.save()

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)


    # API View for partially updating a specific record

    def patch(self, request, id):

        form_data = request.data

        m = Movie.objects.get(id=id)

        serializer_instance = MovieSerializer(
            m,
            data=form_data,
            partial=True
        )

        if serializer_instance.is_valid():

            # Data After validation
            # cleaned_data = serializer_instance.validated_data
            # title = cleaned_data['title']

            serializer_instance.save()

            return Response(serializer_instance.data)

        else:

            return Response(serializer_instance.errors)


    # API View for deleting a specific record

    def delete(self, request, id):

        m = get_object_or_404(Movie, id=id)

        m.delete()

        return Response({"Message": "Movie is Deleted"})