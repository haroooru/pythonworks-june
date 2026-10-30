# from rest_framework import serializers
#
# from movies.models import Movie
#
#
# class MovieSerializer(serializers.Serializer):
#
#     title = serializers.CharField()
#     director = serializers.CharField()
#     language = serializers.CharField()
#     year = serializers.IntegerField()
#     rating = serializers.FloatField()
#     runtime = serializers.IntegerField()
#
#     def create(self, validated_data):
#
#         m = Movie.objects.create(**validated_data)
#
#         return m

from rest_framework import serializers

from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:

        model = Movie

        fields = '__all__'