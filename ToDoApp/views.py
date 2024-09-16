from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Todo,CustomUser
from .serializer import ToDoSerializer

class getMyTodoView(APIView):
    authentication_classes = [JWTAuthentication,]
    permission_classes = [IsAuthenticated,]
    def get(self,request):
        todos = Todo.objects.all()
        serializer = ToDoSerializer(todos,many=True)
        return Response(data=serializer.data)


class CreateTodoView(APIView):
    authentication_classes = [JWTAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    def post(self,request):
        data = request.data
        Todo.objects.create(
            author = request.user,
            todoName=data['todoName'],
            todoDescription=data['todoDescription'],
            isDone=False
        )
        return Response(data={'result':'successfull'})

class EditTodoView(APIView):
    def post(self,request,id):
        data = request.data

        myTodo = Todo.objects.get(id=id)

        try:
            myTodo.todoName = data['todoName']
        except:
            print('*')

        try:
            myTodo.todoDescription = data['todoDescription']
        except:
            print('**')

        try:
            myTodo.isDone = data['isDone']
        except:
            print('***')

        myTodo.save()

        return Response({'detail':'succesfull'})