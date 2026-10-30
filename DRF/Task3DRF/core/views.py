
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from django.shortcuts import get_object_or_404

from .models import Department, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer


class AdminWritePermission:
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_staff


class DepartmentList(APIView):
    permission_classes = [IsAuthenticated, AdminWritePermission]

    def get(self, request):
        departments = Department.objects.all()
        serializer_instance = DepartmentSerializer(departments, many=True)
        return Response(serializer_instance.data)

    def post(self, request):
        serializer_instance = DepartmentSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(
                serializer_instance.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer_instance.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class DepartmentDetail(APIView):
    permission_classes = [IsAuthenticated, AdminWritePermission]

    def get(self, request, id):
        department = get_object_or_404(Department, id=id)
        serializer_instance = DepartmentSerializer(department)
        return Response(serializer_instance.data)

    def put(self, request, id):
        department = get_object_or_404(Department, id=id)
        serializer_instance = DepartmentSerializer(
            department, data=request.data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)

        return Response(
            serializer_instance.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id):
        department = get_object_or_404(Department, id=id)
        department.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeList(APIView):
    permission_classes = [IsAuthenticated, AdminWritePermission]

    def get(self, request):
        employees = Employee.objects.all()
        serializer_instance = EmployeeSerializer(employees, many=True)
        return Response(serializer_instance.data)

    def post(self, request):
        serializer_instance = EmployeeSerializer(data=request.data)

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(
                serializer_instance.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer_instance.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class EmployeeDetail(APIView):
    permission_classes = [IsAuthenticated, AdminWritePermission]

    def get(self, request, id):
        employee = get_object_or_404(Employee, empid=id)
        serializer_instance = EmployeeSerializer(employee)
        return Response(serializer_instance.data)

    def put(self, request, id):
        employee = get_object_or_404(Employee, empid=id)
        serializer_instance = EmployeeSerializer(
            employee, data=request.data
        )

        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)

        return Response(
            serializer_instance.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, id):
        employee = get_object_or_404(Employee, empid=id)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DepartmentEmployees(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        department = get_object_or_404(Department, id=id)
        employees = Employee.objects.filter(department=department)

        department_data = DepartmentSerializer(department).data
        employee_data = EmployeeSerializer(employees, many=True).data

        return Response({
            "department": department_data,
            "employees": employee_data
        })
