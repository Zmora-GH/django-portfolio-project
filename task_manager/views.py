from django.shortcuts import render
from django.shortcuts import redirect
from .models import TaskBoard, Task
from .forms import TaskForm, BoardForm


def view_main(request):
	""" """
	context = {}
	return render(request,'task_manager/main_page.html', context=context)


def view_boards(request):
	""" """
	if request.user.is_authenticated:
		boards = TaskBoard.objects.filter(user=request.user)

		form =  BoardForm()

		context = {
			'board_count': len(boards),
			'boards': boards,
			'form': form,
		}
		return render(request, 'task_manager/boards.html', context=context)
	else:
		return redirect('login_url')


def view_tasks(request, board_id):
	""" """
	tasks = Task.objects.filter(board=board_id)
	stages = Task.STAGE_CHOICE

	form =  TaskForm()

	context = {
		'tasks': tasks,
		'stages': stages,
		'form': form,
	} 
	return render(request, 'task_manager/taskboard.html', context=context)