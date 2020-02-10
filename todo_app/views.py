import logging
import os
from datetime import datetime
from uuid import uuid4

from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.response import Response

from simple_todos.settings import IMAGE_DIR
from todo_app.auth import CustomPerm
from todo_app.models import Todo
from todo_app.serializers import TodoSerializer

logger = logging.getLogger(__name__)


class TodoRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [CustomPerm]
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.data.get('completed'):
            instance.completed_at = datetime.now()
        if request.FILES:
            legacy_file = instance.image_url
            if legacy_file:
                image_delete(legacy_file)
            _, file = request.FILES.items().__next__()
            uploaded_filename = image_upload(file)
            instance.image_url = uploaded_filename

        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        if instance.image_url:
            image_delete(instance.image_url)
        return Response(status=status.HTTP_204_NO_CONTENT)


class TodoListCreateView(ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        if request.FILES:
            _, file = request.FILES.items().__next__()
            uploaded_filename = image_upload(file)
            created_todo = self.queryset.filter(id=serializer.data.get('id')).first()
            created_todo.image_url = uploaded_filename
            created_todo.save()

        result_todo = Todo.objects.filter(id=serializer.data.get('id')).first()
        headers = self.get_success_headers(serializer.data)
        return Response(self.get_serializer(result_todo).data, status=status.HTTP_201_CREATED, headers=headers)


def image_upload(file):
    extension = file.name.split('.')[-1]
    random_filename = uuid4().hex + '.' + extension
    path = IMAGE_DIR + random_filename
    with open(path, '+wb') as dest:
        for chunk in file.chunks():
            dest.write(chunk)

    return random_filename


def image_delete(filename):
    if os.path.isfile(IMAGE_DIR + filename):
        os.remove(IMAGE_DIR + filename)
