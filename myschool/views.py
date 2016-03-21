from .models import Teachers, Students, Subjects
from .serializers import TeachersSerializer, StudentsSerializer, SubjectsSerializer
from rest_framework import generics

# Create your views here.
class ShowTeacherList(generics.ListCreateAPIView):
    queryset = Teachers.objects.all()
    serializer_class = TeachersSerializer
    
class ShowStudentsList(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

class ShowSubjectsList(generics.ListCreateAPIView):
    queryset = Subjects.objects.all()
    serializer_class = SubjectsSerializer