import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        htmlnode = HTMLNode("p", "tagvalue", [], '{"href": "https://www.google.com", "target": "_blank",}')
        node = HTMLNode("p", "tagvalue", [htmlnode, htmlnode], '{"href": "https://www.google.com", "target": "_blank",}')
        node2 = HTMLNode("p", "tagvalue", [htmlnode, htmlnode], '{"href": "https://www.google.com", "target": "_blank",}')
        self.assertEqual(node, node2)

    def test_ne(self):
        htmlnode = HTMLNode("p", "tagvalue", [], '{"href": "https://www.google.com", "target": "_blank",}')
        node = HTMLNode("p", "tagvalue", [htmlnode, htmlnode], '{"href": "https://www.google.com", "target": "_blank",}')
        node2 = HTMLNode("p", "wrongtagvalue", [htmlnode, htmlnode], '{"href": "https://www.google.com", "target": "_blank",}')
        self.assertNotEqual(node, node2)

    def test_ne_2(self):
        htmlnode = HTMLNode("p", "tagvalue", [], '{"href": "https://www.google.com", "target": "_blank",}')
        node = HTMLNode("p", "tagvalue", [], '{"href": "https://www.google.com", "target": "_blank",}')
        node2 = HTMLNode("p", "wrongtagvalue", [htmlnode, htmlnode], '{"href": "https://www.google.com", "target": "_blank",}')
        self.assertNotEqual(node, node2)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_child_nesting(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parent_child_nesting(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],
                        ),
                    ]
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>")

    def test_parent_parent_child_nesting(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
                ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                        ParentNode(
                            "p",
                            [
                                LeafNode("b", "Bold text"),
                                LeafNode(None, "Normal text"),
                                LeafNode("i", "italic text"),
                                LeafNode(None, "Normal text"),
                            ],
                                ),
                    ],
                        ),
                    ]
        )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p></p>")

if __name__ == "__main__":
    unittest.main()


