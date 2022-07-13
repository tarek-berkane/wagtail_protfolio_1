from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import PageChooserPanel, FieldPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel

from apps.category.services import get_skills
from apps.project.services import get_projects

# Create your models here.


class Home(Page):
    max_count = 1
    parent_page_types = []

    description = models.TextField(max_length=200)

    cv_btn = models.ForeignKey(
        "wagtaildocs.Document",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="+",
    )

    page_btn = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        DocumentChooserPanel("cv_btn"),
        PageChooserPanel("page_btn", "page.About"),
    ]

    def get_skills(self):
        return get_skills()

    def get_projects(self):
        return get_projects()


class About(Page):
    text = models.CharField(max_length=200)
