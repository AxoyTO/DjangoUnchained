from django.shortcuts import render, redirect
from django.views import generic
from django.http import HttpResponse
from django.utils import timezone
from .models import Project
from .forms import ProjectForm


# Create your views here.
def projects(request):
    projects = Project.objects.all()
    template = "projects/index.html"
    context = {"projects": projects}
    return render(request, template, context)


def project(request, pk):
    project_object = Project.objects.get(id=pk)
    template = "projects/project.html"
    # tags = project_object.tags.all()
    # reviews = project_object.review_set.all()
    context = {"project": project_object}

    return render(request, template, context)


def create_project(request):
    form = ProjectForm()
    template = "projects/project-form.html"

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("projects:projects")

    context = {"form": form}
    return render(request, template, context)


def update_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    template = "projects/project-form.html"

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect(f"../project/{pk}")

    context = {"form": form}
    return render(request, template, context)


def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    template = "projects/delete.html"

    if request.method == "POST":
        project.delete()
        return redirect("projects:projects")

    context = {"object": project}

    return render(request, template, context)
