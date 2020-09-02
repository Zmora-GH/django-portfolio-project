
from django.urls import path
from .views import view_main, BoardsView, TasksView

urlpatterns = [
    path('', view_main, name='view_main'),
    path('boards/', BoardsView.as_view(), name='view_boards'),
    path('taskboard/<int:board_id>', TasksView.as_view(), name='view_tasks'),
]