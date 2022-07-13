from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock


class Header(blocks.StructBlock):
    HEADER_TYPE = (
        ("h2", "Header 2"),
        ("h3", "Header 3"),
        ("h4", "Header 4"),
    )

    type = blocks.ChoiceBlock(choices=HEADER_TYPE, default="h2")
    title = blocks.CharBlock(max_length=255)

    class Meta:
        template = "blocks/header.html"


class BlockQuote(blocks.StructBlock):
    content = blocks.TextBlock()

    class Meta:
        template = "blocks/blockquote.html"


class Image(blocks.StructBlock):
    photo = ImageChooserBlock(required=False)
    caption = blocks.CharBlock(required=False, max_length=50)

    class Meta:
        template = "blocks/image.html"


class Terminal(blocks.StructBlock):
    code = blocks.CharBlock(max_length=255)

    class Meta:
        template = "blocks/terminal.html"
