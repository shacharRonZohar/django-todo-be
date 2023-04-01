from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Todo
from .serializers import TodoSerializer


@api_view(['GET'])
def api_overview(request):
    api_urls = {
        'List': '/todos/',
        'Create': '/create/',
    }

    return Response(api_urls)


@api_view(['GET'])
def get_todo_list(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def create_todo(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def get_todo_by_id(request):
    print(request.data)
    # todo = Todo.objects.get(id=pk)
    # serializer = TodoSerializer(todo, many=False)

    return Response(request.data)