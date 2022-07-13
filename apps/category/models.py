from audioop import reverse
from turtle import heading
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.models import Page, Site

from modelcluster.fields import ParentalKey, ParentalManyToManyField


class ProjectTag(models.Model):
    text = models.CharField(max_length=255)
    feed_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    show = models.BooleanField(default=False)

    panels = [
        MultiFieldPanel(
            [
                FieldPanel("text"),
                ImageChooserPanel("feed_image"),
                FieldPanel("show"),
            ],
            heading="Tag paramters",
        )
    ]

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return Page.objects.filter(slug="projects").first().url

    class Meta:
        abstract = True


@register_snippet
class ProjectType(ProjectTag):
    def get_absolute_url(self):
        url = super().get_absolute_url()
        return url + f"?project_type={self.id}"


@register_snippet
class Language(ProjectTag):
    def get_absolute_url(self):
        url = super().get_absolute_url()
        return url + f"?project_language={self.id}"


@register_snippet
class Library(ProjectTag):
    def get_absolute_url(self):
        url = super().get_absolute_url()
        return url + f"?prjoect_library={self.id}"


@register_snippet
class Framework(ProjectTag):
    def get_absolute_url(self):
        url = super().get_absolute_url()
        return url + f"?project_framework={self.id}"


@register_snippet
class Database(ProjectTag):
    def get_absolute_url(self):
        url = super().get_absolute_url()
        return url + f"?project_framework={self.id}"


@register_snippet
class Other(ProjectTag):
    def get_absolute_url(self):
        url = super().get_absolute_url()
        return url + f"?project_framework={self.id}"
