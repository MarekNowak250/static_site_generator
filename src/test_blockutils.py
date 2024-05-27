import unittest

from blockutils import ( markdown_to_blocks, block_to_block_type, markdown_to_html_node,
                            block_type_heading,
                            block_type_paragraph,
                            block_type_code,
                            block_type_quote,
                            block_type_unordered_list,
                            block_type_ordered_list,)

from parentnode import ParentNode
from leafnode import LeafNode

class TextBlockUtils(unittest.TestCase):
    def test_markdown_to_blocks(self):
        result = markdown_to_blocks(
        f'''

This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items''')

        self.assertEqual(result, [
            'This is **bolded** paragraph', 
            'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', 
            '* This is a list\n* with items'
            ])
        
    def test_block_to_block_type_heading(self):
        result = block_to_block_type("###### ex")
        self.assertEqual(block_type_heading, result)

    def test_block_to_block_type_code(self):
        result = block_to_block_type("```ex```")
        self.assertEqual(block_type_code, result)
    
    def test_block_to_block_type_quote(self):
        result = block_to_block_type(">ex\n>test")
        self.assertEqual(block_type_quote, result)
    
    def test_block_to_block_type_unordered_list(self):
        result = block_to_block_type("- ex\n- ex")
        self.assertEqual(block_type_unordered_list, result)
    
    def test_block_to_block_type_ordered_list(self):
        result = block_to_block_type("1. ex\n2. two")
        self.assertEqual(block_type_ordered_list, result)

    def test_block_to_block_type_paragraph(self):
        result = block_to_block_type("1. ex\n3. two")
        self.assertEqual(block_type_paragraph, result)
        
        result = block_to_block_type(">.ex\n2. two")
        self.assertEqual(block_type_paragraph, result)
        
        result = block_to_block_type("*ex")
        self.assertEqual(block_type_paragraph, result)
        
        result = block_to_block_type("-ex")
        self.assertEqual(block_type_paragraph, result)

        result = block_to_block_type("#######")
        self.assertEqual(block_type_paragraph, result)

        result = block_to_block_type("txt")
        self.assertEqual(block_type_paragraph, result)

    def test_markdown_to_html_node(self):
        result = markdown_to_html_node("# test\n\ntext\n\n1. item1\n2. item2\n\n## head2")
        self.assertEqual(result.to_html(),
            ParentNode(tag="div", children=[
                LeafNode(tag="h1", value="test"),
                LeafNode(tag="p", value="text"),
                ParentNode(tag="ol", children=[
                    LeafNode(tag="li", value="item1"),
                    LeafNode(tag="li", value="item2"),
                ]),
                LeafNode(tag="h2", value="head2"),
            ]).to_html()
        )
        