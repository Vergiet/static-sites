
from inline_markdown import *
from block_markdown import convert_node_prefix

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    new_nodes = []
    temp_nodes = []
    temp_nodes.extend(
        split_nodes_link(
            split_nodes_image(
                split_nodes_delimiter(
                    split_nodes_delimiter(
                        split_nodes_delimiter(
                            nodes, "**", TextType.BOLD
                        ), "_", TextType.ITALIC
                    ), "`", TextType.CODE
                )
            )
        )
    )

    new_nodes.extend(
        convert_node_prefix(
            convert_node_prefix(
                convert_node_prefix(
                    temp_nodes, "(?:^\-\s)(.*)", TextType.LIST
                    ), r"(?:^\d\.\s)(.*)", TextType.LIST
                ), r"(?:^\>\s)(.*)", TextType.TEXT
            )
        )
    return new_nodes