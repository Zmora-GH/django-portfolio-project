from django.urls import path
from .views import hub_page 

urlpatterns = [
    path('', hub_page, name='hub'),
]