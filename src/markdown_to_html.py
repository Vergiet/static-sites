from block_markdown import markdown_to_blocks
from block_to_blocktype import block_to_blocktype
from text_to_textnodes import text_to_textnodes
from main import text_node_to_html_node
from blocknode import BlockNode
from htmlnode import ParentNode, LeafNode
from blocktype import BlockType
from textnode import TextType, TextNode
from block_markdown import convert_node_prefix


def markdown_to_html_node(markdown):

    blocks = []
    for block in markdown_to_blocks(markdown):
        blocks.append(BlockNode(block, block_to_blocktype(block)))
    tag = "p"
    block_parents = []
    html_nodes = []
    html_sub_nodes = []
    for block in blocks:
        if (block.type == BlockType.PARAGRAPH or block.type == BlockType.HEADING) and len(block.value) > 0:
            for text_node in text_to_textnodes(block.value):
                html_nodes.append(text_node_to_html_node(remove_lineendings(text_node)))

        if block.type == BlockType.CODE:
            tag = "pre"

            code_lines = "\n".join(block.value.splitlines()[1:-1])+"\n"
            html_sub_nodes.append(text_node_to_html_node(TextNode(code_lines, TextType.TEXT)))
            html_nodes = [ParentNode("code", html_sub_nodes)]

        if block.type == BlockType.UNORDERED_LIST:
            for line in block.value.splitlines():
                for text_node in text_to_textnodes(line):
                    html_sub_nodes.append(text_node_to_html_node(trim_lineendings(text_node)))
            html_nodes = [ParentNode("ul", html_sub_nodes)]

        if block.type == BlockType.ORDERED_LIST:
            for line in block.value.splitlines():
                for text_node in text_to_textnodes(line):
                    html_sub_nodes.append(text_node_to_html_node(trim_lineendings(text_node)))
            html_nodes = [ParentNode("ol", html_sub_nodes)]

        if block.type == BlockType.QUOTE:
            for line in block.value.splitlines():
                for text_node in text_to_textnodes(line):
                    html_sub_nodes.append(text_node_to_html_node(trim_lineendings(text_node)))
            html_nodes = [ParentNode("blockquote", html_sub_nodes)]

        if len(html_nodes) > 0:
            block_parents.append(ParentNode(tag, html_nodes))
            html_nodes = []
            html_sub_nodes = []

    return ParentNode("div", block_parents)


def remove_lineendings(text_node):
    text_node.text = text_node.text.replace("\n", " ")
    return text_node

def ltrim_lineendings(text_node):
    text_node.text = text_node.text.lstrip("\n")
    return text_node

def trim_lineendings(text_node):
    text_node.text = text_node.text.strip("\n")
    return text_node

def text_to_children(text):
    pass