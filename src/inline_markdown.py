from textnode import TextNode, TextType
from constants import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(URL_REGEX_SPLIT, text)

def extract_markdown_links(text):
    return re.findall(URL_REGEX_SPLIT, text)

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        match_list = re.findall(LINK_REGEX_FULL, old_node.text)

        if len(match_list) == 0:
            split_nodes.append(old_node)
            new_nodes.extend(split_nodes)
            continue

        for sections in match_list:
            if not sections[1][0] == '[' or not sections[1][-1] == ')':
                raise ValueError("invalid markdown, incorrect link syntax")

            if sections[0]: # sections 0 is always a text type
                split_nodes.append(TextNode(sections[0], TextType.TEXT))

            if sections[1]: # 1 is always a link type
                alt_text, url = extract_markdown_links(sections[1])[0]
                split_nodes.append(TextNode(alt_text, TextType.LINK, url))

            if sections[2]: # sections 2 is always a text type
                split_nodes.append(TextNode(sections[2], TextType.TEXT))

        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        match_list = re.findall(IMG_REGEX_FULL, old_node.text)

        if len(match_list) == 0:
            split_nodes.append(old_node)
            new_nodes.extend(split_nodes)
            continue

        for sections in match_list:
            if not sections[1][0] == '!' or not sections[1][-1] == ')':
                raise ValueError("invalid markdown, incorrect image syntax")

            if sections[0]: # sections 0 is always a text type
                split_nodes.append(TextNode(sections[0], TextType.TEXT))

            if sections[1]: # 1 is always a link type
                alt_text, url = extract_markdown_links(sections[1])[0]
                split_nodes.append(TextNode(alt_text, TextType.IMAGE, url))

            if sections[2]: # sections 2 is always a text type
                split_nodes.append(TextNode(sections[2], TextType.TEXT))

        new_nodes.extend(split_nodes)
    return new_nodes

