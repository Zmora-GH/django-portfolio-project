from django.contrib.auth import views
from django.urls import path
from .views import account_view, registration_view

urlpatterns = [
    path('', account_view, name='account_url'),
    path('registration/', registration_view, name='reg_user_url'),

    path('login/', 
    	views.LoginView.as_view(template_name='account/login.html'), 
    	name='login_url'),
    path('logout/', 
    	views.LogoutView.as_view(template_name='account/logged_out.html'), 
    	name='logout_url'),
    path('pass_change/', 
    	views.PasswordChangeView.as_view(template_name='account/pass_change.html'), 
    	name='password_change'),
    path('pass_change/done/', 
    	views.PasswordChangeDoneView.as_view(template_name='account/pass_change_done.html'), 
    	name='password_change_done')
]