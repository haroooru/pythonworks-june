from rest_framework import serializers
from rest_framework.response import Response
from .models import Employee

class EmployeeSerializer(serializers.Serializer):
    empid=serializers.IntegerField()
    name=serializers.CharField(max_length=30)
    age=serializers.IntegerField()
    place=serializers.CharField(max_length=30)

    gender_choices=[
        ('male','Male'),('female','Female')  #1.save the data into the table(db value),2.display it in interface(display value)
    ]

    gender=serializers.ChoiceField(choices=gender_choices)

    joining_date = serializers.DateField()
    #joining_date=models.DateField(auto_now_add=True)  #it will add date value automatically
    # joining_date=models.DateTimeField(auto_now_add=True)   #it will add date value automatically

    salary=serializers.IntegerField()
    designation=serializers.CharField(max_length=30)
    image=serializers.ImageField()


    #After validation and before saving

    def create(self,validated_data):
        e=Employee.objects.create(**validated_data)
        return e    #return employee object

    #After validation and before saving

    def update(self,i,validated_data):  #i=instance

        i.empid=validated_data.get('empid',i.empid)
        i.name=validated_data.get('name',i.name)
        i.age=validated_data.get('age', i.age)
        i.place=validated_data.get('place', i.place)
        i.gender=validated_data.get('gender', i.gender)
        i.joining_date=validated_data.get('joining_date', i.joining_date)
        i.salary=validated_data.get('salary', i.salary)
        i.designation=validated_data.get('designation', i.designation)

        i.save()
        return i



    def validate(self,data):
        if data['age']<=0:
            raise serializers.ValidationError('Age must be positive')
        # if data['age']<18:
        #     raise serializers.ValidationError('Age must be greater than 18')
        return data