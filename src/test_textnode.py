import unittest

from textnode import (
    text_type_text,
    text_type_code,
    text_type_bold,
    text_type_image,
    text_type_link,
    text_type_italic,
    TextNode)

from textnodeutils import TextNodeUtils


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node2", "bold")
        self.assertNotEqual(node, node2)
    
    def test_not_eq_text_type(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold2")
        self.assertNotEqual(node, node2)
    
    def test_not_eq_url(self):
        node = TextNode("This is a text node", "bold", "https://example.com")
        node2 = TextNode("This is a text node", "bold","https://example2.com")
        self.assertNotEqual(node, node2)

    def test_split_nodes_delimiter_one_bold_block(self):
        node = TextNode("This is text with a **bold block** word", "text")
        result = TextNodeUtils().split_nodes_delimiter([node], "**", "bold")
        self.assertEqual([
            TextNode("This is text with a ", text_type_text),
            TextNode("bold block", text_type_bold),
            TextNode(" word", text_type_text),
        ], result)

    def test_split_nodes_delimiter_one_code_block(self):
        node = TextNode("This is text with a `code block` word", "text")
        result = TextNodeUtils().split_nodes_delimiter([node], "`", "code")
        self.assertEqual([
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ], result)

    def test_split_nodes_delimiter_two_code_block(self):
        node = TextNode("`code`This is text with a `code block` word", "text")
        result = TextNodeUtils().split_nodes_delimiter([node], "`", "code")
        self.assertEqual([
            TextNode('code', text_type_code),
            TextNode("This is text with a ", text_type_text),
            TextNode("code block", text_type_code),
            TextNode(" word", text_type_text),
        ], result)

    def test_split_nodes_throw_when_no_closure(self):
        node = TextNode("`code This is text with a `code block` word", "text")
        action = lambda : TextNodeUtils().split_nodes_delimiter([node], "`", "code")
        self.assertRaises(Exception, action)

    def test_split_nodes_images_no_images(self):
        node = TextNode("text no image", "text")
        result = TextNodeUtils().split_nodes_image([node])
        self.assertEqual([node], result)

    def test_split_nodes_images_no_links(self):
        node = TextNode("text no links", "text")
        result = TextNodeUtils().split_nodes_link([node])
        self.assertEqual([node], result)

    def test_split_nodes_images(self):
        node = TextNode("![first](test) text ![second](image)![third](image)end", "text")
        result = TextNodeUtils().split_nodes_image([node])
        self.assertEqual(result,
            [
                TextNode("first", text_type_image, "test"),
                TextNode(" text ", text_type_text),
                TextNode("second", text_type_image, "image"),
                TextNode("third", text_type_image, "image"),
                TextNode("end", text_type_text)]
        )

    def test_split_nodes_links(self):
        node = TextNode("[first](test) text [second](link)[third](link)end", "text")
        result = TextNodeUtils().split_nodes_link([node])
        self.assertEqual(result,
            [
                TextNode("first", text_type_link, "test"),
                TextNode(" text ", text_type_text),
                TextNode("second", text_type_link, "link"),
                TextNode("third", text_type_link, "link"),
                TextNode("end", text_type_text)]
        )

    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"
        result = TextNodeUtils().text_to_textnodes(text)
        
        self.assertEqual(result,
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ]
        )

if __name__ == "__main__":
    unittest.main()