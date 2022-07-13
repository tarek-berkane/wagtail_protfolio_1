from django.db import models
from django.http import HttpRequest
from django.core.paginator import Paginator

from wagtail.admin.edit_handlers import (
    TabbedInterface,
    ObjectList,
    FieldPanel,
    StreamFieldPanel,
    MultiFieldPanel,
)
from wagtail.core.models import Page
from wagtail.core.blocks import RichTextBlock
from wagtail.core.fields import StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, route

from modelcluster.fields import ParentalManyToManyField
from apps.category.services import get_frameworks, get_languages, get_project_types

import apps.project.blocks as project_blocks
from apps.project.forms import ProjectForm


class ProjectIndex(RoutablePageMixin, Page):
    max_count = 1
    parent_page_types = [
        "page.Home",
    ]
    subpage_types = [
        "project.Project",
    ]

    # ROUTING
    @route(r"^$")  # will override the default Page serving mechanism
    def current_events(self, request: HttpRequest):
        queryset = None
        if request.GET:
            form = ProjectForm(request.GET)
            if form.is_valid():
                queryset = self.project_search(**form.cleaned_data)
            else:
                queryset = self.project_search()

        else:
            form = ProjectForm()
            queryset = self.project_search()

        if request.GET.get("p"):
            page_number = request.GET.get("p")
            page = self.paginate(queryset, page_number)
        else:
            page = self.paginate(queryset)

        context = {}
        context["form"] = form
        context["page"] = page
        context["parameters_url"] = self.build_url_query(**request.GET)

        return self.render(
            request,
            context_overrides=context,
        )

    # OTHER METHODS
    def project_search(
        self,
        text: str = None,
        sort_type: str = None,
        project_type: str = None,
        project_language: str = None,
        project_framework: str = None,
        **kwargs,
    ):

        query = self.get_children().live()

        if text:
            query = query.filter(title__contains=text)

        return query

    def build_url_query(
        self,
        text: str = None,
        sort_type: str = None,
        project_type: str = None,
        project_language: str = None,
        project_framework: str = None,
        **kwargs,
    ):

        parameters = "?"

        if text:
            parameters = parameters + f"text={text[0]}&"

        if sort_type:
            parameters = parameters + f"sort_type={sort_type[0]}&"

        if project_type:
            parameters = parameters + f"project_type={project_type[0]}&"

        if project_language:
            parameters = parameters + f"project_language={project_language[0]}&"

        if project_framework:
            parameters = parameters + f"project_framework={project_framework[0]}&"

        return parameters

    def paginate(self, queryset, page_number=1):
        result_paginated = Paginator(queryset, 9)
        page = result_paginated.get_page(page_number)
        return page


# Create your models here.
class Project(Page):
    parent_page_types = [
        "project.ProjectIndex",
    ]
    subpage_types = []

    # Properties
    RICH_TEXT_FEATURES = ["bold", "italic", "h2", "ol", "ul", "document-link", "link"]

    # CONTENT
    show_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        related_name="+",
        null=True,
        blank=True,
    )

    content = StreamField(
        [
            ("header", project_blocks.Header()),
            ("image", project_blocks.Image()),
            ("block_quote", project_blocks.BlockQuote()),
            ("terminal", project_blocks.Terminal()),
            ("Rich_text", RichTextBlock()),
        ]
    )

    # META-DATA
    project_type = ParentalManyToManyField(to="category.ProjectType", blank=True)
    frameworks = ParentalManyToManyField(to="category.Framework", blank=True)
    languages = ParentalManyToManyField(to="category.Language", blank=True)
    libraries = ParentalManyToManyField(to="category.Library", blank=True)
    databases = ParentalManyToManyField(to="category.Database", blank=True)
    others = ParentalManyToManyField(to="category.Other", blank=True)

    short_description = models.CharField(max_length=100)
    github_link = models.URLField(blank=True)
    demo_link = models.URLField(blank=True)

    # PANELS
    content_panels = Page.content_panels + [
        ImageChooserPanel("show_image"),
        StreamFieldPanel("content"),
    ]

    metadata_panels = [
        FieldPanel("short_description"),
        MultiFieldPanel(
            [
                FieldPanel("github_link"),
                FieldPanel("demo_link"),
            ],
            heading="Links",
        ),
        MultiFieldPanel(
            [
                FieldPanel("project_type"),
                FieldPanel("languages"),
                FieldPanel("frameworks"),
                FieldPanel("libraries"),
                FieldPanel("databases"),
                FieldPanel("others"),
            ],
            heading="Tags",
        ),
        # tags
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading="Content"),
            ObjectList(metadata_panels, heading="Meta-data"),
            ObjectList(Page.promote_panels, heading="Promote"),
            ObjectList(Page.settings_panels, heading="Settings", classname="settings"),
        ]
    )

    template = "project/project.html"
