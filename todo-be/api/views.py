from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Todo
from .serializers import TodoSerializer


@api_view(['GET'])
def getTodoList(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def createTodo(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
