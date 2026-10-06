from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response

from myapp.models import Employee
from myapp.serializers import EmployeeSerializer

class EmployeeList(APIView):

    def get(self, request):

        qs = Employee.objects.all()

        serializer_instance = EmployeeSerializer(
            qs,
            many=True
        )

        return Response(
            serializer_instance.data
        )



class EmployeeCreate(APIView):

    def post(self, request):

        serializer_instance = EmployeeSerializer(
            data=request.data
        )

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(
                serializer_instance.data
            )

        else:

            return Response(
                serializer_instance.errors
            )





def update(self, instance, validated_data):

    instance.empid = validated_data.get(
        'empid',
        instance.empid
    )

    instance.name = validated_data.get(
        'name',
        instance.name
    )

    instance.age = validated_data.get(
        'age',
        instance.age
    )

    instance.place = validated_data.get(
        'place',
        instance.place
    )

    instance.gender = validated_data.get(
        'gender',
        instance.gender
    )

    instance.joining_date = validated_data.get(
        'joining_date',
        instance.joining_date
    )

    instance.salary = validated_data.get(
        'salary',
        instance.salary
    )

    instance.designation = validated_data.get(
        'designation',
        instance.designation
    )

    instance.save()

    return instance






from django.shortcuts import get_object_or_404

class EmployeeDetail(APIView):

    def get(self, request, i):

        e = get_object_or_404(
            Employee,
            id=i
        )

        serializer_instance = EmployeeSerializer(e)

        return Response(
            serializer_instance.data
        )



class EmployeeUpdate(APIView):

    def put(self, request, i):

        e = get_object_or_404(
            Employee,
            id=i
        )

        serializer_instance = EmployeeSerializer(
            e,
            request.data
        )

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(
                serializer_instance.data
            )

        else:

            return Response(
                serializer_instance.errors
            )



class EmployeePartialUpdate(APIView):

    def patch(self, request, i):

        e = get_object_or_404(
            Employee,
            id=i
        )

        serializer_instance = EmployeeSerializer(
            e,
            request.data,
            partial=True
        )

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(
                serializer_instance.data
            )

        else:

            return Response(
                serializer_instance.errors
            )






class EmployeeDelete(APIView):

    def delete(self, request, i):

        e = get_object_or_404(
            Employee,
            id=i
        )

        e.delete()

        return Response({
            "message": "deleted"
        })





