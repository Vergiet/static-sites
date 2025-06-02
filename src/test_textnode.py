import unittest

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


if __name__ == "__main__":
    unittest.main()