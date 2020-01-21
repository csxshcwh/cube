from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('regist/', views.regist, name='regist'),
]