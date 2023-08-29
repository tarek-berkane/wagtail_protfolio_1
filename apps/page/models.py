from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import PageChooserPanel, FieldPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting

# panels
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

# blocks
import apps.blocks as project_blocks
from wagtail.core.blocks import RichTextBlock

# fileds
from wagtail.core.fields import StreamField

# services
from apps.category.services import get_skills
from apps.project.services import get_projects


@register_setting
class SocialMediaSettings(BaseSetting):
    github = models.URLField(help_text="Your github page", blank=True, null=True)
    linkedin = models.URLField(help_text="Your linkedin account", blank=True, null=True)
    youtube = models.URLField(
        help_text="Your youtube chanel",
        blank=True,
        null=True,
    )
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)


class Home(Page):
    max_count = 1
    # parent_page_types = []

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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["page_section"] = "home"
        return context


class About(Page):
    parent_page_types = [
        "page.Home",
    ]

    salutation = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    description = models.TextField()
    auth_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )

    content = StreamField(
        [
            ("header", project_blocks.Header()),
            ("Rich_text", RichTextBlock()),
            ("image", project_blocks.Image()),
        ]
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("salutation"),
                FieldPanel("sub_title"),
                FieldPanel("description"),
                ImageChooserPanel("auth_image"),
            ],
            heading="Main",
        ),
        StreamFieldPanel("content"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["page_section"] = "about"
        return context
