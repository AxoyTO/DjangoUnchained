from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Task


class CustomLoginView(LoginView):
    template_name = "base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tasks")


class CustomLogoutView(LogoutView):
    next_page = "login"


class TaskList(LoginRequiredMixin, generic.list.ListView):
    model = Task
    context_object_name = "tasks"
    login_url = "login"  # No need if set LOGIN_URL = "login" in settings.py

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        context["count"] = context["tasks"].filter(complete=False).count()
        return context


class TaskDetail(LoginRequiredMixin, generic.detail.DetailView):
    model = Task
    context_object_name = "task"
    template_name = "base/task.html"


class TaskCreate(generic.edit.CreateView):
    model = Task
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("tasks")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(generic.edit.UpdateView):
    model = Task
    fields = ["title", "description", "complete"]
    success_url = reverse_lazy("tasks")


class TaskDelete(generic.edit.DeleteView):
    model = Task
    context_object_name = "task"
    template_name = "base/task_delete.html"
    success_url = reverse_lazy("tasks")
