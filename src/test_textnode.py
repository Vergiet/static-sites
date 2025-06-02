import unittest

from main import text_node_to_html_node
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.Bold, 'boot.dev')
        node2 = TextNode("This is a text node", TextType.Bold, 'boot.dev')
        self.assertEqual(node, node2)

    def test_ne(self):
        node = TextNode("This is also a text node", TextType.Bold, 'boot.dev')
        node2 = TextNode("This is a text node", TextType.Bold, 'boot.dev')
        self.assertNotEqual(node, node2)

    def test_ne_2(self):
        node = TextNode("This is a text node", TextType.Link, 'boot.dev')
        node2 = TextNode("This is a text node", TextType.Bold, 'boot.dev')
        self.assertNotEqual(node, node2)


    def test_text(self):
        node = TextNode("This is a text node", TextType.Text)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node.to_html(), "This is a text node")

    def test_bold(self):
        node = TextNode("This is a bold node", TextType.Bold)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")
        self.assertEqual(html_node.to_html(), "<b>This is a bold node</b>")

    def test_italic(self):
        node = TextNode("This is an italic node", TextType.Italic)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")
        self.assertEqual(html_node.to_html(), "<i>This is an italic node</i>")

    def test_code(self):
        node = TextNode("This is a code block", TextType.Code)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code block")
        self.assertEqual(html_node.to_html(), "<code>This is a code block</code>")

    def test_link(self):
        node = TextNode("This is a link node", TextType.Link, "boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.to_html(), '<a  href="boot.dev" alt="This is a link node">This is a link node</a>')


    def test_img(self):
        node = TextNode("This is an img node", TextType.Image, "boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "This is an img node")
        self.assertEqual(html_node.to_html(), '<img  src="boot.dev" alt="This is an img node" >')


if __name__ == "__main__":
    unittest.main()