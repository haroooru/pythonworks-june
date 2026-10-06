from rest_framework import serializers

# Import Employee model
from .models import Employee


# ============================================================
# EMPLOYEE SERIALIZER
# ============================================================

class EmployeeSerializer(serializers.Serializer):

    # Employee ID
    empid = serializers.IntegerField()

    # Employee name
    name = serializers.CharField(max_length=30)

    # Employee age
    age = serializers.IntegerField()

    # Employee place
    place = serializers.CharField(max_length=30)

    # Gender choices
    gender_choices = [
        ('male', 'Male'),
        ('female', 'Female')
    ]

    # Employee gender
    gender = serializers.ChoiceField(
        choices=gender_choices
    )

    # Employee joining date
    joining_date = serializers.DateField()

    # Employee salary
    salary = serializers.IntegerField()

    # Employee designation
    designation = serializers.CharField(max_length=50)


    # --------------------------------------------------------
    # CREATE
    # --------------------------------------------------------
    # This method tells DRF how to create an Employee object
    # when serializer_instance.save() is called.
    def create(self, validated_data):

        # Create Employee object using the validated data
        employee = Employee.objects.create(**validated_data)

        # Return the newly created Employee object
        return employee


    # --------------------------------------------------------
    # UPDATE
    # --------------------------------------------------------

    # Update an existing Employee object
    def update(self, i, validated_data):

        # Update each field.
        # .get() takes the new value if it is provided.
        # If not provided, keep the old value.

        i.empid = validated_data.get('empid', i.empid)

        i.name = validated_data.get('name', i.name)

        i.age = validated_data.get('age', i.age)

        i.place = validated_data.get('place', i.place)

        i.gender = validated_data.get('gender', i.gender)

        i.joining_date = validated_data.get(
            'joining_date',
            i.joining_date
        )

        i.salary = validated_data.get(
            'salary',
            i.salary
        )

        i.designation = validated_data.get(
            'designation',
            i.designation
        )

        # Save the updated employee object
        i.save()

        # Return updated employee object
        return i