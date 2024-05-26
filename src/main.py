from textnode import TextNode
from textnodeutils import TextNodeUtils
from markdownutils import extract_markdown_images, extract_markdown_links, markdown_to_blocks

def main():
    node = TextNode(
    "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
    "text",
    )

    print(markdown_to_blocks(
f'''

This is **bolded** paragraph

  This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items'''))
    #print(TextNodeUtils().split_nodes_image([node]))

    #print(TextNodeUtils().text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"))
    # print(extract_markdown_links("This is text with an [image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and [another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"))

if __name__ == "__main__":
    main()