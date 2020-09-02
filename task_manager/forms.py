from django import forms
from .models import Task, TaskBoard


class TaskForm(forms.ModelForm):
	class Meta:
		prefix = 'task_form'
		model = Task
		fields = ['title', 'body', 'stage', 'bg']
		widgets = {
			'body': forms.Textarea()
		}


class BoardForm(forms.ModelForm):
	class Meta:
		prefix = 'board_form'
		model = TaskBoard
		fields = ['name',]
