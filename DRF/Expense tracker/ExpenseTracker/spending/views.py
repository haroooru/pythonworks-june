from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer, ExpenseSerializer


# API View for creating a new user account
class RegisterView(APIView):
    def post(self, request):
        serializer_instance = UserSerializer(data=request.data)

        if serializer_instance.is_valid():
            user = serializer_instance.save()
            Token.objects.get_or_create(user=user)
            return Response(
                {'message': 'User registered successfully'},
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer_instance.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


# API View for reading current logged-in user details
class GetUserDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer_instance = UserSerializer(user)
        return Response(serializer_instance.data)


# API View for adding an expense
class AddExpense(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer_instance = ExpenseSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save(owner=request.user)
            return Response(
                serializer_instance.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer_instance.errors,
            status=status.HTTP_400_BAD_REQUEST
        )