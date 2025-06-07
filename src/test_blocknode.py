import unittest
from block_to_blocktype import (
    block_to_blocktype,
)
from blocktype import BlockType

class TestBlockType(unittest.TestCase):
    def test_block_to_paragraph_1(self):
        self.assertEqual(block_to_blocktype("This is **bolded** paragraph"), BlockType.PARAGRAPH)

    def test_block_to_paragraph_2(self):
        self.assertEqual(block_to_blocktype("This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line"), BlockType.PARAGRAPH)

    def test_block_to_unordered_list(self):
        self.assertEqual(block_to_blocktype("- This is a list\n- with items"), BlockType.UNORDERED_LIST)

    def test_block_to_code(self):
        self.assertEqual(block_to_blocktype("```\nthis is a code block\n```"), BlockType.CODE)

    def test_block_to_ordered_list(self):
        self.assertEqual(block_to_blocktype("1. This is an\n2. Ordered list"), BlockType.ORDERED_LIST)

    def test_block_to_heading(self):
        self.assertEqual(block_to_blocktype("# heading 1"), BlockType.HEADING)

    def test_block_to_heading(self):
        self.assertEqual(block_to_blocktype("## heading 2"), BlockType.HEADING)

    def test_block_to_headingh(self):
        self.assertEqual(block_to_blocktype("### heading 3"), BlockType.HEADING)

    def test_block_to_qoute(self):
        self.assertEqual(block_to_blocktype("> This is a quote\n> with items"), BlockType.QUOTE)

if __name__ == "__main__":
    unittest.main()