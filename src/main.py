#!/usr/bin/env python
from textnode import TextNode, TextType
from htmlnode import LeafNode

from constants import *



def text_node_to_html_node(text_node):
    props = None
    tag = None
    match text_node.text_type:
        case TextType.BOLD:
            tag = "b"
        case TextType.ITALIC:
            tag = "i"
        case TextType.CODE:
            tag = "code"
        case TextType.LINK:
            tag = "a"
            props = {
                "href": text_node.url,
                "alt": text_node.text
            }
        case TextType.IMAGE:
            tag = "img"
            props = {
                "src": text_node.url,
                "alt": text_node.text
            }

    return LeafNode(tag, text_node.text, props)

print('\n')

def main():
    print(TextNode('This is some anchor text', (TextType.LINK), 'https://www.boot.dev'))




if __name__=="__main__":
    main()