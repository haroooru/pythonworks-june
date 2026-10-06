from rest_framework import serializers
from myapp.models import Employee


class EmployeeSerializer(serializers.Serializer):

    empid = serializers.IntegerField()

    name = serializers.CharField(max_length=30)

    age = serializers.IntegerField()

    place = serializers.CharField(max_length=30)

    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female')
    ]

    gender = serializers.ChoiceField(
        choices=gender_choices
    )

    joining_date = serializers.DateField()

    salary = serializers.IntegerField()

    designation = serializers.CharField()

    def create(self, validated_data):
        e = Employee.objects.create(
            **validated_data
        )

        return e