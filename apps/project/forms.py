from django import forms

from apps.category.services import get_frameworks, get_languages, get_project_types


class ProjectForm(forms.Form):
    SORT_TYPE = (
        ("D", "Date"),
        ("P", "Popularty"),
        ("T", "Trend"),
    )

    text = forms.CharField(max_length=50, required=False)
    sort_type = forms.ChoiceField(
        choices=SORT_TYPE,
        initial="D",
        required=True,
    )
    project_type = forms.ChoiceField(choices=get_project_types)
    project_language = forms.ChoiceField(choices=get_languages)
    project_framework = forms.ChoiceField(choices=get_frameworks)

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields["text"].widget.attrs[
            "class"
        ] = "input input-sm input-bordered border-primary w-full"

        self.fields["sort_type"].widget.attrs[
            "class"
        ] = "select select-bordered select-sm w-full"

        self.fields["project_type"].widget.attrs[
            "class"
        ] = "select select-bordered select-sm w-full"

        self.fields["project_language"].widget.attrs[
            "class"
        ] = "select select-bordered select-sm w-full"

        self.fields["project_framework"].widget.attrs[
            "class"
        ] = "select select-bordered select-sm w-full"
