from apps.category.models import (
    Database,
    Framework,
    Language,
    Library,
    Other,
    ProjectType,
)


def get_skills():
    database = Database.objects.filter(show=True)
    languages = Language.objects.filter(show=True)
    frameworks = Framework.objects.filter(show=True)
    libraries = Library.objects.filter(show=True)
    others = Other.objects.filter(show=True)

    skills_set = set()
    skills_set = skills_set.union(set(database))
    skills_set = skills_set.union(set(languages))
    skills_set = skills_set.union(set(frameworks))
    skills_set = skills_set.union(set(libraries))
    skills_set = skills_set.union(set(others))

    return skills_set


def get_frameworks():
    frameworks = Framework.objects.all()
    data_set = [(-1, 'any')]
    data_set += [(framework.id, framework.text) for framework in frameworks]
    return data_set


def get_languages():
    languages = Language.objects.all()
    data_set = [(-1, 'any')]
    data_set += [(language.id, language.text) for language in languages]
    return data_set


def get_project_types():
    project_types = ProjectType.objects.all()
    data_set = [(-1, 'any')]
    data_set += [(project_type.id, project_type.text) for project_type in project_types]
    return data_set
