from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.task_list, name="tasks")
]
