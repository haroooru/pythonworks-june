from rest_framework import serializers

from django.contrib.auth.models import User

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:

        model = Movie

        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = [
            'username',
            'password',
            'email',
            'first_name',
            'last_name'
        ]