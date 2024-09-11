from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from .models import Todo,CustomUser
from .serializer import ToDoSerializer

class getMyTodoView(APIView):
    def get(self,request):
        todos = Todo.objects.all()
        serializer = ToDoSerializer(todos,many=True)
        return Response(data=serializer.data)