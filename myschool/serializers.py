from rest_framework import serializers
from .models import Teachers, Students, Subjects

class TeachersSerializer (serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ('id', 'teacher_name')

class StudentsSerializer (serializers.ModelSerializer):
    class Meta:
        model = Students
        exclude = tuple()
        
class SubjectsSerializer (serializers.ModelSerializer):
    class Meta:
        model = Subjects