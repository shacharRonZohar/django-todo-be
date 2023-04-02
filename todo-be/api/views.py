from rest_framework import generics

from .serializers import TodoSerializer
from base.models import Todo


# With generics
class TodoList(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


"""
# With mixins and a generic view
class TodoList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class TodoDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



# With view classes
class TodoList(APIView):
    serializer_class = TodoSerializer

    def get(self, request):
        todos = Todo.objects.all()
        serializer = self.serializer_class(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoDetail(APIView):
    serializer_class = TodoSerializer

    @staticmethod
    def get_object(pk):
        try:
            return Todo.objects.get(id=pk)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        todo = self.get_object(pk=pk)
        serializer = self.serializer_class(todo, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        todo = self.get_object(pk=pk)
        serializer = self.serializer_class(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        todo = self.get_object(pk=pk)
        todo.delete()
        return Response('Todo item deleted', status=status.HTTP_204_NO_CONTENT)
        
        
# With decorators
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
    # main = Todo.objects.get(id=pk)
    # serializer = TodoSerializer(main, many=False)

    return Response(request.data)
"""
