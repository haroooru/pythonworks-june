from rest_framework import serializers
from employees.models import Employee


class EmployeeSerializers(serializers.Serializer):
    employee_id = serializers.IntegerField()
    employee_name = serializers.CharField(max_length=100)
    employee_age = serializers.IntegerField()
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('Other', 'Other')
    ]
    employee_gender = serializers.ChoiceField(choices=gender_choices)
    employee_salary = serializers.IntegerField()
    employee_joining_date = serializers.DateField()
    employee_designation = serializers.CharField(max_length=100)
    employee_image= serializers.ImageField()

    # After validation and before saving
    def create(self, validated_data):
        employee = Employee.objects.create(**validated_data)
        return employee

    # After validation and before saving
    def update(self,ins,validated_data):
        ins.employee_id = validated_data.get('employee_id',ins.employee_id)
        ins.employee_name = validated_data.get('employee_name',ins.employee_name)
        ins.employee_age = validated_data.get('employee_age',ins.employee_age)
        ins.employee_gender = validated_data.get('employee_gender',ins.employee_gender)
        ins.employee_salary = validated_data.get('employee_salary',ins.employee_salary)
        ins.employee_joining_date = validated_data.get('employee_joining_date',ins.employee_joining_date)
        ins.employee_designation=validated_data.get('employee_designation',ins.employee_designation)
        ins.employee_image= validated_data.get('employee_image',ins.employee_image)
        ins.save()
        return ins