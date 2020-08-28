
from django.urls import path
from .views import view_main, view_boards, view_tasks

urlpatterns = [
    path('', view_main, name='view_main'),
    path('boards/', view_boards, name='view_boards'),
    path('taskboard/', view_tasks, name='view_tasks'),
]