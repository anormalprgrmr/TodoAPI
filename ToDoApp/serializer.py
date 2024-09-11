from rest_framework import serializers
from .models import todo,CustomUser

class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = todo
        fields = ['todoName','todoDescription','isDone','date']