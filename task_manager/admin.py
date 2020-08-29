from django.contrib import admin
from .models import TaskBoard, Task


class TaskInline(admin.TabularInline):
    model = Task


class TaskPanel(admin.ModelAdmin):
	list_display = ['title', 'last_change', 'pub_date']
	list_display_links = ['title']
	search_fields = ['title']


class BoardPanel(admin.ModelAdmin):
	list_display = ['name', 'user', 'last_change', 'pub_date']
	list_display_links = ['name']
	search_fields = ['name','user']
	inlines = [TaskInline]


admin.site.register(TaskBoard, BoardPanel)
admin.site.register(Task, TaskPanel)

