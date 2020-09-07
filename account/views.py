from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def registration_view(request):
	""" Просто вьюха для регистрации """

	form = UserCreationForm()
	if request.method == 'POST':
		b_form = UserCreationForm(request.POST)
		if form.is_valid:
			new_user = b_form.save()
			return HttpResponseRedirect(reverse('login_url'))
	context = {'form': form, }
	return render(request, 'account/register.html', context=context)

