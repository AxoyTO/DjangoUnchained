from django.shortcuts import render
from django.http import HttpResponse


project_list = [
    {
        "id": "1",
        "title": "Ecommerce Website",
        "description": "Fully functional ecommerce website",
        "topRated": True,
    },
    {
        "id": "2",
        "title": "Portfolio Website",
        "description": "A personal website to write articles and display work",
        "topRated": False,
    },
    {
        "id": "3",
        "title": "Social Network",
        "description": "An open source project built by the community",
        "topRated": True,
    },
]

# Create your views here.
def projects(request):
    context = {"projects": project_list}
    return render(request, "projects/index.html", context)


def project(request, pk):
    project_object = None
    try:
        project_object = [project for project in project_list if project["id"] == pk][0]
    except IndexError:
        pass
    context = {"project": project_object}
    return render(request, "projects/project.html", context)
