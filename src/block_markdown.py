from textnode import TextType, TextNode
import re

def markdown_to_blocks(raw_markdown):
    md_blocks = []
    new_block = []
    for line in raw_markdown.splitlines():
        if line == "":
            if len(new_block) > 0:
                md_blocks.append('\n'.join(new_block))
            new_block = []
        else:
            new_block.append(line)
    md_blocks.append('\n'.join(new_block))
    return md_blocks

def convert_node_prefix(old_nodes, prefix, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        x = None
        x = re.findall(prefix, old_node.text)
        if x:
            new_nodes.append(TextNode(x[0], text_type))
        else:
            new_nodes.append(old_node)

    return new_nodes

