from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseBadRequest

from .models import TaskBoard, Task
from .forms import TaskForm, BoardForm


def view_main(request):
	""" """
	context = {}
	return render(request,'task_manager/main_page.html', context=context)


class BoardsView(View, LoginRequiredMixin):
	""" """
	login_url='login_url'

	def get(self, request):
		""" """
		boards = TaskBoard.objects.filter(user=request.user)
		form =  BoardForm()
		context = {
			'board_count': len(boards),
			'boards': boards,
			'form': form,
		}
		return render(request, 'task_manager/boards.html', context=context)

	def post(self, request):
		board_form = BoardForm(request.POST)
		if board_form.is_valid():
			new_board = board_form.save()
			new_board.user = request.user
			new_board.save()
			return redirect('view_tasks', board_id=new_board.id)
		return redirect('view_boards')


class TasksView(View, LoginRequiredMixin):
	""" """
	login_url='login_url'

	def get(self, request, board_id):
		""" """
		tasks = Task.objects.filter(board=board_id)
		stages = Task.STAGE_CHOICE
		form_n = TaskForm()
		form_e = TaskForm()
		form_d = TaskForm()
		context = {
			'tasks': tasks,
			'stages': stages,
			'form_n': form_n,
			'form_e': form_e,
			'form_d': form_d,
		} 
		return render(request, 'task_manager/taskboard.html', context=context)

	def post(self, request, board_id):
		""" """
		if request.POST['opcode'] == '2':
			x_form = TaskForm(request.POST)
			if x_form.is_valid():
				new_task = x_form.save()
				return redirect('view_tasks', board_id=board_id)
		elif request.POST['opcode'] == '1':
			x_form = TaskForm(request.POST)
			if x_form.is_valid():
				task = Task.objects.get(id=int(request.POST['id']))
				task.title = x_form.cleaned_data.get('title')
				task.body = x_form.cleaned_data.get('body')
				task.stage = x_form.cleaned_data.get('stage')
				task.save() 
				return redirect('view_tasks', board_id=board_id)
		elif request.POST['opcode'] == '0':
			Task.objects.get(id=int(request.POST['id'])).delete()
			return redirect('view_tasks', board_id=board_id)
		else:
			return HttpResponseBadRequest('Oops! This opcode is wrong!')
		return redirect('view_tasks', board_id=board_id)

