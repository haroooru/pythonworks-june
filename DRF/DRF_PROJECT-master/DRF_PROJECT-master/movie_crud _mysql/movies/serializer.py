from rest_framework import serializers
from movies.models import Movie

#
# class MovieSerializers(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     director = serializers.CharField(max_length=200)
#     language = serializers.CharField(max_length=200)
#     year = serializers.IntegerField()
#     rating = serializers.FloatField()
#     runtime = serializers.IntegerField()
#
#     def create(self, validated_data):
#         movie = Movie.objects.create(**validated_data)
#         return movie
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.director = validated_data.get('director', instance.director)
#         instance.language = validated_data.get('language', instance.language)
#         instance.year = validated_data.get('year', instance.year)
#         instance.rating = validated_data.get('rating', instance.rating)
#         instance.runtime = validated_data.get('runtime', instance.runtime)
#         instance.save()
#         return instance
class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields={
        #     'title','director','language'.........
        # }
        fields='__all__'

        def validate(self,data):
            if data['title'] is None:
                raise serializers.ValidationError({'title':"This field is required."})
            if data['rating'] == 0:
                raise serializers.ValidationError({'rating':"This field must be greater than 0."})