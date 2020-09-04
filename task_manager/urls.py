from django.views.generic import TemplateView
from django.urls import path
from .views import BoardsView, TasksView, drop_task

urlpatterns = [
	path('', TemplateView.as_view(template_name='task_manager/main_page.html'), name='view_main'),
	path('xmlhttp/', drop_task, name='view_drop'),
	path('boards/', BoardsView.as_view(), name='view_boards'),
	path('taskboard/<int:board_id>', TasksView.as_view(), name='view_tasks'),
]
