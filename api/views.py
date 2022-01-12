from django.shortcuts import render
from rest_framework.utils import serializer_helpers
from .serializers import TaskSerializer
from rest_framework import generics
from .models import Task

# Function Based Views
"""
@api_view(['GET'])
def say_hello(request):
    return Response({"message":"Hello from Django"})
"""

# Class Based Views
# Get --> ListAPIView
# GET<id> --> RetrieveAPIView
# POST --> CreateAPIView
# PUT<id> --> UpdateAPIView
# DELETE<id> --> DestroyAPIView
class TaskList(generics.ListCreateAPIView):
    # Query data from the database
    queryset = Task.objects.all()
    # Define a serializer class (ModelSeriallizer)
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    # Query data from the database
    queryset = Task.objects.all()
    # Define a serializer class (ModelSeriallizer)
    serializer_class = TaskSerializer