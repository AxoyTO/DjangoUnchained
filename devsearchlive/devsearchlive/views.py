from django.shortcuts import render


def about(request):
    template = "about.html"
    return render(request, template)


def contact(request):
    template = "contact.html"
    return render(request, template)
