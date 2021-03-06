import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.http import HttpResponseBadRequest
from django.http import HttpResponseForbidden
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.views.generic import View

from .models import TaskBoard, Task
from .forms import TaskForm, BoardForm


def drop_task(request):
	"""Вьюшка для изменения категории тасков при 
	перетаскивании. Принимает Ajax пост-запрос из js."""

	if request.method == 'POST':
		data = json.loads(request.body)
		task = Task.objects.get(id=data['id'])
		task.stage = data['stage']
		task.save()
		return JsonResponse({'status': 200})
	return JsonResponse()


class BoardsView(LoginRequiredMixin, View):
	""" Вьюха для списка досок"""

	login_url='login_url'

	def get(self, request):
		""" Рендерит список досок текущего пользователя"""
		
		boards = TaskBoard.objects.filter(user=request.user)
		form =  BoardForm()
		context = {
			'board_count': len(boards),
			'boards': boards,
			'form': form,
		}
		return render(request, 'task_manager/boards.html', context=context)

	def post(self, request):
		""" Принимает пост-запрос из формы создания доски.
		Если форма валидна, создаем новую доску, привязываем ее
		к текущему пользователю  и сохроняет"""

		board_form = BoardForm(request.POST)
		if board_form.is_valid():
			new_board = board_form.save()
			new_board.user = request.user
			new_board.save()
			return redirect('view_tasks', board_id=new_board.id)
		return redirect('view_boards')


class TasksView(LoginRequiredMixin, View):
	""" Вьюха для тасок на доске """

	login_url='login_url'

	def get(self, request, board_id):
		""" Рендерит таски указаной доски """

		try:
			if TaskBoard.objects.get(id=board_id).user != request.user:
				return HttpResponseForbidden('<h1>403 Forbidden</h1>')
			tasks = Task.objects.filter(board=board_id)
			stages = Task.STAGE_CHOICE
			form = TaskForm()
			context = {
				'tasks': tasks,
				'stages': stages,
				'form': form,
			}
			return render(request, 'task_manager/taskboard.html', context=context)
		except TaskBoard.DoesNotExist:
			return HttpResponseNotFound('<h1>404 Not Found</h1>')

	def post(self, request, board_id):
		""" Принимает пост-запрос. В зависимости от opcode,
		обрабатываютя три операции или выдает 400 Bad Request: 
		[0] - delete Удаление 
		[1] - edit	 Редактирование 
		[2] - create Создание """
		
		if request.POST['opcode'] == '2':
			x_form = TaskForm(request.POST)
			if x_form.is_valid():
				Task.objects.create(
					title=x_form.cleaned_data.get('title'),
					body=x_form.cleaned_data.get('body'),
					stage=x_form.cleaned_data.get('stage'),
					bg=x_form.cleaned_data.get('bg'),
					board=TaskBoard(id=board_id))
				return redirect('view_tasks', board_id=board_id)

		elif request.POST['opcode'] == '1':
			x_form = TaskForm(request.POST)
			if x_form.is_valid():
				Task.objects.filter(id=int(request.POST['id'])).update(
					title=x_form.cleaned_data.get('title'),
					body=x_form.cleaned_data.get('body'),
					stage=x_form.cleaned_data.get('stage'),
					bg=x_form.cleaned_data.get('bg'),
					board=TaskBoard(id=board_id))
				return redirect('view_tasks', board_id=board_id)

		elif request.POST['opcode'] == '0':
			Task.objects.get(id=int(request.POST['id'])).delete()
			return redirect('view_tasks', board_id=board_id)

		else:
			return HttpResponseBadRequest('<h1>Oops! This opcode is wrong!</h1>')
