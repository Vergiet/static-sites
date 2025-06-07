from enum import Enum

class TextType(Enum):
    BOLD = "BOLD"
    ITALIC = "ITALIC"
    CODE = "CODE"
    LINK = "LINK"
    LIST = "LIST"
    IMAGE = "IMAGE"
    TEXT = "TEXT"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.url = url
        self.text = text
        self.text_type = text_type

    def __eq__(self, other):
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


