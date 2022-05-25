from .serializers import TaskSerializer
from rest_framework import generics, permissions
from .models import Task

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
    permission_classes = [permissions.IsAuthenticated]