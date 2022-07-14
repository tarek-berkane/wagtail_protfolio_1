
from django.core.paginator import Paginator


def paginate(queryset, page_number=1, item_by_page=9):
    result_paginated = Paginator(queryset, item_by_page)
    page = result_paginated.get_page(page_number)
    return page


def build_url_query(
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