from django.shortcuts import render

# Import Employee model
from .models import Employee

# Import APIView from Django REST Framework
from rest_framework.views import APIView

# Import Response from Django REST Framework
from rest_framework.response import Response

# Import EmployeeSerializer
from .serializers import EmployeeSerializer


# ============================================================
# 1. GET ALL EMPLOYEES
# ============================================================

class EmployeeList(APIView):

    def get(self, request):

        # Read all employee records from Employee table
        qs = Employee.objects.all()

        # Serialize multiple Employee objects
        # many=True because there can be multiple records
        serializer_instance = EmployeeSerializer(
            qs,
            many=True
        )

        # Send serialized data to client
        return Response(
            data=serializer_instance.data
        )


# ============================================================
# 2. CREATE NEW EMPLOYEE
# ============================================================

class EmployeeCreate(APIView):

    def post(self, request):

        # request.data contains data sent by the client
        # DRF converts the incoming JSON into Python-native data

        # Pass incoming data to serializer
        serializer_instance = EmployeeSerializer(
            data=request.data
        )

        # Validate incoming data
        if serializer_instance.is_valid():

            # Save validated data into database
            serializer_instance.save()

            # Send success response
            return Response({
                "message": "created"
            })

        else:

            # Send validation errors if data is invalid
            return Response(
                serializer_instance.errors
            )



# ============================================================
# 3. GET A SPECIFIC EMPLOYEE
# ============================================================

# APIView for reading a specific record
class EmployeeDetail(APIView):

    def get(self, request, i):

        # Read a specific employee using the ID
        # If the employee does not exist, return 404
        e = get_object_or_404(Employee, id=i)

        # Convert the Employee model object
        # into Python-native data
        serializer_instance = EmployeeSerializer(e)

        # Send the serialized data as response
        return Response(
            serializer_instance.data
        )


# ============================================================
# 5. UPDATE EMPLOYEE - PUT
# ============================================================

# APIView for updating an existing employee record
class EmployeeUpdate(APIView):

    def put(self, request, id):

        # Get the existing employee from the database
        e = Employee.objects.get(id=id)

        # Pass the existing employee object AND
        # the new data to the serializer
        serializer_instance = EmployeeSerializer(
            e,
            data=request.data
        )

        # Validate the updated data
        if serializer_instance.is_valid():

            # Save the updated employee to the database
            serializer_instance.save()

            # Return the updated employee data
            return Response(
                serializer_instance.data
            )

        else:

            # Return validation errors
            return Response(
                serializer_instance.errors
            )



class EmployeePartialUpdate(APIView):

    def patch(self, request, i):

        e = get_object_or_404(Employee, id=i)

        serializer_instance = EmployeeSerializer(
            e,
            request.data,
            partial=True
        )

        if serializer_instance.is_valid():

            serializer_instance.save()
            return Response(serializer_instance.data)

        else:
            return Response(serializer_instance.errors)