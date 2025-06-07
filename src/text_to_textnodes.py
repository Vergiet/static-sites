
from inline_markdown import *


def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = []
    new_nodes.extend(split_nodes_link(split_nodes_image(split_nodes_delimiter(split_nodes_delimiter(split_nodes_delimiter(nodes, "**", TextType.BOLD), "_", TextType.ITALIC), "`", TextType.CODE))))
    return new_nodes