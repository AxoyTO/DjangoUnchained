from django.contrib import admin

# Register your models here.
from .models import Project, Review, Tag


class ProjectAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "created",
    ]
    list_filter = ["created"]
    search_fields = ["title"]
    fieldsets = [
        ("About the project", {"fields": ["title", "description"]}),
        ("Links", {"fields": ["demo_link", "source_link"]}),
        ("Votes", {"fields": ["vote_total", "vote_ratio"]}),
        ("Tags", {"fields": ["tags"]}),
    ]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Review)
admin.site.register(Tag)
