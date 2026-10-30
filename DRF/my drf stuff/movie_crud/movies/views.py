from django.db.models import Q

from django.contrib.auth.models import User

from rest_framework import (
    mixins,
    generics,
    viewsets,
    status
)

from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework.filters import SearchFilter

from .models import Movie

from .serializers import (
    MovieSerializer,
    UserSerializer
)


# Generics


class MovieListCreate(
        generics.ListCreateAPIView):

    queryset = Movie.objects.all()

    serializer_class = MovieSerializer


class MovieRetrieveUpdateDelete(
        generics.RetrieveUpdateDestroyAPIView):

    queryset = Movie.objects.all()

    serializer_class = MovieSerializer


# Viewsets


class MovieView(
        viewsets.ModelViewSet):

    queryset = Movie.objects.all()

    serializer_class = MovieSerializer


# Search API View


class SearchAPIView(APIView):

    def get(self, request):

        #fetches data coming from request url

        data = self.request.query_params.get(
            'search'
        )

        #filters movie records having title matching with data

        m = Movie.objects.filter(
            Q(title__icontains=data) |
            Q(director__icontains=data) |
            Q(language__icontains=data)
        )

        #converts the qs into native type using Serializer class

        serializer_instance = MovieSerializer(
            m,
            many=True
        )

        #returns response as json using Response Class

        return Response(
            serializer_instance.data,
            status=status.HTTP_200_OK
        )


# Search API View using SearchFilter


class MovieSearchAPIView(
        generics.ListAPIView):

    queryset = Movie.objects.all()

    serializer_class = MovieSerializer

    filter_backends = [SearchFilter]

    search_fields = [
        'title',
        'director',
        'language'
    ]


# Registration


class RegisterAPIView(APIView):

    def post(self, request):

        form_data = request.data

        serializer_instance = UserSerializer(
            data=form_data
        )

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(
                serializer_instance.data,
                status=status.HTTP_201_CREATED
            )

        else:

            return Response(
                serializer_instance.data,
                status=status.HTTP_400_BAD_REQUEST
            )