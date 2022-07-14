from django.db import models
from django.http import HttpRequest

from wagtail.admin.edit_handlers import (
    TabbedInterface,
    ObjectList,
    FieldPanel,
    StreamFieldPanel,
    MultiFieldPanel,
)
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from modelcluster.fields import ParentalManyToManyField
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.images.edit_handlers import ImageChooserPanel


from apps.project.forms import ProjectForm
from apps.project.utils import build_url_query, paginate

# blocks
import apps.blocks as project_blocks
from wagtail.core.blocks import RichTextBlock


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

        if request.GET:
            form = ProjectForm(request.GET)
            if form.is_valid():
                queryset = Project.project_search(**form.cleaned_data)
            else:
                queryset = Project.project_search()
        else:
            form = ProjectForm()
            queryset = Project.project_search()

        if request.GET.get("p"):
            page_number = request.GET.get("p")
            page = paginate(queryset, page_number)
        else:
            page = paginate(queryset)

        context = {}
        context["form"] = form
        context["page"] = page
        context["parameters_url"] = build_url_query(**request.GET)

        return self.render(
            request,
            context_overrides=context,
        )

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["page_section"] = "projects"
        return context


class Project(Page):
    template = "project/project.html"

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

    @staticmethod
    def project_search(
        text: str = None,
        sort_type: str = None,
        project_type: str = None,
        project_language: str = None,
        project_framework: str = None,
        **kwargs,
    ):

        query = Project.objects.live().specific()

        if text:
            query = query.filter(title__contains=text)

        if project_type and project_type != "any":
            query = query.specific().filter(project_type__in=project_type)

        if project_language and project_language != "any":
            query = query.specific().filter(languages__in=project_language)

        if project_framework and project_framework != "any":
            query = query.specific().filter(frameworks__in=project_framework)

        return query

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["page_section"] = "projects"
        return context
