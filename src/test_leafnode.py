import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html_no_value(self):
        node = LeafNode(None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_no_tag(self):
        node = LeafNode("test")
        value = node.to_html()
        self.assertEqual("test", value)
    
    def test_to_html_no_props(self):
        node = LeafNode("test", "c")
        value = node.to_html()
        self.assertEqual("<c>test</c>", value)
    
    def test_to_html(self):
        node = LeafNode("test", "c", {"href": "https://www.example.com"})
        value = node.to_html()
        self.assertEqual("<c href=\"https://www.example.com\">test</c>", value)


if __name__ == "__main__":
    unittest.main()