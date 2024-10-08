from rest_framework import serializers
from .models import Todo,CustomUser

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['author','todoName','todoDescription','isDone','date']