from audioop import reverse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy


from .models import Task
from .forms import UserRegisterForm


class CustomLoginView(LoginView):
    template_name = "base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("tasks")


class CustomLogoutView(LogoutView):
    next_page = "login"


class RegisterView(generic.edit.CreateView):
    template_name = "base/register.html"
    success_url = reverse_lazy("tasks")
    # success_message = "Your profile was created successfully!"
    redirect_authenticated_user = True
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        print(user)
        if user is not None:
            print("not none.")
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("tasks")
        return super(RegisterView, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, generic.list.ListView):
    model = Task
    context_object_name = "tasks"
    login_url = "login"  # No need if set LOGIN_URL = "login" in settings.py

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        context["count"] = context["tasks"].filter(complete=False).count()

        search_input = self.request.GET.get("search-area") or ""
        if search_input:
            context["tasks"] = context["tasks"].filter(title__startswith=search_input)

        context["search_input"] = search_input
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
