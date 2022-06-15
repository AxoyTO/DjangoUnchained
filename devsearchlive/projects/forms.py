from django.forms import ModelForm, RadioSelect
from .models import Project, Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        exclude = ["vote_total", "vote_ratio"]

        def __init__(self, *args, **kwargs) -> None:
            super(ProjectForm, self).__init__(*args, **kwargs)

            for key, value in self.fields.items():
                value.widget.attrs.update({"class": "input"})

            # self.fields["title"].widget.attrs.update({"class": "input"})


class ReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        self.fields["project"].widget.attrs["class"] = "form-control"

    class Meta:
        model = Review
        fields = "__all__"
        # exclude = ["project"]
        widgets = {"value": RadioSelect()}
