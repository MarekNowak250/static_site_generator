import unittest

from markdownutils import extract_markdown_images, extract_markdown_links, markdown_to_blocks

class TextMarkdownUtils(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev)"
        )
        self.assertListEqual(
            [
                ("link", "https://boot.dev"),
                ("another link", "https://blog.boot.dev"),
            ],
            matches,
        )

    def test_markdown_to_blocks(self):
        result = markdown_to_blocks(
        f'''

        This is **bolded** paragraph

            This is another paragraph with *italic* text and `code` here
        This is the same paragraph on a new line

        * This is a list
        * with items''')
        self.assertEqual(result, [
            ['This is **bolded** paragraph'], 
            ['This is another paragraph with *italic* text and `code` here', 'This is the same paragraph on a new line'], 
            ['* This is a list', '* with items']
            ])