from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse


def registration_view(request):
    form = UserCreationForm()
    if request.method == 'POST':
        b_form = UserCreationForm(request.POST)
        if form.is_valid:
            new_user = b_form.save()
            return HttpResponseRedirect(reverse('login_url'))
    context = {'form': form, }
    return render(request, 'account/register.html', context=context)

def account_view(request):
	context = {}
	return render(request, 'account/account_page.html', context=context)
