from django.shortcuts import render
# import django_filter
from .models import Todo
from .serializers import TodoSerializer
from rest_framework import viewsets,filters
# Create your views here.

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('id')
    serializer_class = TodoSerializer
