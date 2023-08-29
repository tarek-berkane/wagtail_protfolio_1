from django.http import HttpRequest
from django import forms
from django.shortcuts import render
from django.views.generic import ListView

from apps.project.models import Project, ProjectIndex
from apps.category.models import Framework


def get_all_framework():
    frameworks = Framework.objects.all()
    frameworks_list = [(framework.id, framework.text) for framework in frameworks]
    frameworks_list.insert(("any", "Any"))
    return frameworks_list


class ProjectForm(forms.ModelForm):
    text = forms.CharField(max_length=50)
    framework = forms.ChoiceField(choices=get_all_framework)


def search(request: HttpRequest):
    print("HERE")
    get_args: dict = request.GET

    form = ProjectForm(get_args)

    objects = Project.objects.filter(live=True)

    if get_args.get("project_framework"):
        framework_id = get_args.get("project_framework")
        objects = objects.filter(frameworks__in=framework_id)

    context = {}
    context["objects"] = objects
    context["form"] = form

    return render(request, "project/search.html", context)
