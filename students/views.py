from django.shortcuts import render
from .models import Students
from .serializers import StudentSerializer
from rest_framework import viewsets
# Create your views here.
class StudentView(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer