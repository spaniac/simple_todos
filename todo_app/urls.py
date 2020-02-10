from django.urls import path

from todo_app.views import TodoRUDView, TodoListCreateView

urlpatterns = [
    path('', TodoListCreateView.as_view()),
    path('<int:pk>', TodoRUDView.as_view()),
]
