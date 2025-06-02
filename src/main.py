#!/usr/bin/env python
from textnode import TextNode, TextType

print("hello world")


def main():
    print(TextNode('This is some anchor text', (TextType.Link), 'https://www.boot.dev'))




if __name__=="__main__":
    main()