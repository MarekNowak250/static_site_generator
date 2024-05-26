import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props = {"href": "https://www.google.com", "target": "_blank"})
        htmlProps = node.props_to_html()
        self.assertEqual(" href=\"https://www.google.com\" target=\"_blank\"",htmlProps)

    def test_props_to_html_props_empty(self):
        node = HTMLNode()
        htmlProps = node.props_to_html()
        self.assertEqual("", htmlProps)
    
    def test_repr(self):
        node = HTMLNode("tag", "value", "children", props = {"target": "_blank"})
        self.assertNotEqual("tag value children {\"target\": \"_blank\"}", repr(node))


if __name__ == "__main__":
    unittest.main()