from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class TaskBoard(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, 
		on_delete=models.CASCADE)
	name = models.CharField(max_length=32)
	pub_date = models.DateTimeField(auto_now_add=True)
	last_change = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-pub_date']
		verbose_name = 'Board'
		verbose_name_plural = 'Boards'

	def __str__(self):
		return self.name


class Task(models.Model):
	STAGE_CHOICE= (
		(1, '1: Idea'),
		(2, '2: Task'),
		(3, '3: In Progress'),
		(4, '4: Comleted'))
	title = models.CharField(max_length=32)
	body = models.CharField(max_length=185)
	stage = models.IntegerField(choices=STAGE_CHOICE, default=1)
	pub_date = models.DateTimeField(auto_now_add=True)
	last_change = models.DateTimeField(auto_now=True)
	board = models.ForeignKey(TaskBoard, on_delete=models.CASCADE,
		related_name='tasks')

	class Meta:
		ordering = ['-last_change']
		verbose_name = 'Task'
		verbose_name_plural = 'Tasks'

	def __str__(self):
		return self.title
