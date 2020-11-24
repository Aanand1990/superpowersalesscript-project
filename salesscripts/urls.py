from django.urls import path, include
from . import views


urlpatterns = [
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('create', views.create, name='create'),
    path('<int:salescript_id>', views.script, name='script'),
]