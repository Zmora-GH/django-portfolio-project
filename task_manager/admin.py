from django.contrib import admin
from .models import TaskBoard, Task


class TaskInline(admin.TabularInline):
    model = Task


class BoardPanel(admin.ModelAdmin):
	list_display = ['name', 'user', 'last_change', 'pub_date']
	list_display_links = ['name']
	search_fields = ['name','user']
	inlines = [TaskInline]


admin.site.register(TaskBoard, BoardPanel)
