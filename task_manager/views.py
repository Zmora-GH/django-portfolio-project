from django.shortcuts import render


def view_main(request):
	""" """
	context = {}
	return render(request,'task_manager/main_page.html', context=context)


def view_boards(request):
	""" """
	context = {}
	return render(request, 'task_manager/boards.html', context=context)


def view_tasks(request):
	""" """
	context = {}
	return render(request, 'task_manager/taskboard.html', context=context)