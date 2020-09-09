from django.db import models
from django.conf import settings


class TaskBoard(models.Model):
	""" Модель доски с задачами. Привязана к пользователю.
	Поле task_count обновляется при создании/удалении задачи."""

	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, 
		on_delete=models.CASCADE)
	name = models.CharField(max_length=32)
	task_count = models.IntegerField(default=0)
	pub_date = models.DateTimeField(auto_now_add=True)
	last_change = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-pub_date']
		verbose_name = 'Board'
		verbose_name_plural = 'Boards'

	def __str__(self):
		return self.name


class Task(models.Model):
	"""Модель задачи. Привязана к доске. 
	Цвета задаются классами bg1-5, которые описываются в css.(?)"""

	STAGE_CHOICE = (
		(1, 'Idea'), (2, 'Task'),
		(3, 'In Progress'), (4, 'Comleted'),
	)
	COLOR_CHOICE = (
		('bg1', 'Red'), ('bg2', 'Green'),
		('bg3', 'Orange'), ('bg4', 'Lilac'),
		('bg5', 'Blue'),
	)
	title = models.CharField(max_length=32)
	body = models.CharField(max_length=185)
	stage = models.IntegerField(choices=STAGE_CHOICE, default=1)
	bg = models.CharField(max_length=3, choices=COLOR_CHOICE, default='bg5')
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

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		tc = Task.objects.filter(board=self.board).count()
		TaskBoard.objects.filter(id=self.board.id).update(task_count=tc)

	def delete(self, *args, **kwargs):
		super().delete(*args, **kwargs)
		tc = Task.objects.filter(board=self.board).count()
		TaskBoard.objects.filter(id=self.board.id).update(task_count=tc)
