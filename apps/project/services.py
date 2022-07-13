from apps.project.models import Project


def get_projects():
    projects = Project.objects.all().live().order_by("-first_published_at")[:6]
    return projects



