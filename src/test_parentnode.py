import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def get_children(self):
        return [
                LeafNode("Bold text", "b"),
                LeafNode("Normal text"),
                LeafNode("italic text", "i"),
                LeafNode("Normal text"),
            ]

    def test_to_html_no_value(self):
        node = ParentNode(self.get_children(), tag=None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_no_value(self):
        node = ParentNode(children=None, tag="test")
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_only_leaves(self):
        node = ParentNode(
            tag="p", children=self.get_children()
        )

        value = node.to_html()
        self.assertEqual("<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>", value)
    
    def test_to_html_nested_parent(self):
        children = self.get_children()
        children.append(ParentNode(tag="a", children=self.get_children()))

        node = ParentNode(
            tag="p", children=children, props={"test": "val"}
        )

        value = node.to_html()
        self.assertEqual("<p test=\"val\"><b>Bold text</b>Normal text<i>italic text</i>Normal text<a><b>Bold text</b>Normal text<i>italic text</i>Normal text</a></p>", value)

    def test_to_html_2lvl_nesting(self):
        children_2lvl = self.get_children()
        parentNode2 = ParentNode(tag="f", children=self.get_children())
        children_2lvl.append(parentNode2)

        children_1lvl = self.get_children()
        parentNode1 = ParentNode(tag="a", children=children_2lvl)
        children_1lvl.append(parentNode1)

        node = ParentNode(
            tag="p", children=children_1lvl, props={"test": "val"}
        )

        value = node.to_html()
        self.assertEqual("<p test=\"val\"><b>Bold text</b>Normal text<i>italic text</i>Normal text<a><b>Bold text</b>Normal text<i>italic text</i>Normal text<f><b>Bold text</b>Normal text<i>italic text</i>Normal text</f></a></p>", value)

if __name__ == "__main__":
    unittest.main()