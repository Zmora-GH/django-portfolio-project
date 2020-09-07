from django import forms

from .models import Task, TaskBoard


class TaskForm(forms.ModelForm):
	""" Форма для таски """

	class Meta:
		prefix = 'task_form'
		model = Task
		fields = ['title', 'body', 'stage', 'bg']
		widgets = {
			'body': forms.Textarea()
		}


class BoardForm(forms.ModelForm):
	""" Форма для доски """

	class Meta:
		prefix = 'board_form'
		model = TaskBoard
		fields = ['name',]
