#!/usr/bin/env python
from textnode import TextNode, TextType
from htmlnode import LeafNode



def text_node_to_html_node(text_node):
    props = None
    tag = None
    match text_node.text_type:
        case TextType.Bold:
            tag = "b"
        case TextType.Italic:
            tag = "i"
        case TextType.Code:
            tag = "code"
        case TextType.Link:
            tag = "a"
            props = {
                "href": text_node.url,
                "alt": text_node.text
            }
        case TextType.Image:
            tag = "img"
            props = {
                "src": text_node.url,
                "alt": text_node.text
            }

    return LeafNode(tag, text_node.text, props)


def main():
    print(TextNode('This is some anchor text', (TextType.Link), 'https://www.boot.dev'))




if __name__=="__main__":
    main()