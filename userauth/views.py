#from django.shortcuts import render
from .models import SignUp
#from angularprofile.serializers import AngularUserSerializer
# Create your views here.
from rest_framework import generics

class AngularUserList(generics.ListCreateAPIView):
    queryset = SignUp.objects.all()
    #serializer_class = AngularUserSerializer