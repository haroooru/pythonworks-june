from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RecipeSerializer



class RecipeCreate(APIView):
    def post(self, request):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


# created = 201
# error = 404 supposed to be used



# from .models import Recipe
# class RecipeDetail(APIView):
#     def get(self,request,id):
#         recipe = Recipe.object.get(id=id)
#         serializer = RecipeSerializer(Recipe)
#         return Response(serializer.data)