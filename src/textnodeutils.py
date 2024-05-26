from leafnode import LeafNode
from markdownutils import extract_markdown_images, extract_markdown_links

from textnode import (
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
    TextNode)

class TextNodeUtils:
    dict = {
        text_type_text: lambda text_node : LeafNode(value=text_node.text),
        text_type_bold: lambda text_node : LeafNode(value=text_node.text, tag="b"),
        text_type_italic: lambda text_node : LeafNode(value=text_node.text, tag="i"),
        text_type_code: lambda text_node : LeafNode(value=text_node.text, tag="code"),
        text_type_link: lambda text_node : LeafNode(value=text_node.text, tag="a", props={"href": text_node.url}),
        text_type_image: lambda text_node : LeafNode(value="", tag="img",
                                              props = { "src": text_node.url, "alt": text_node.text} ),
    }
     
    def text_node_to_html_node(self, text_node):
        if text_node.text in self.dict:
            return self.dict[text_node.text_type](text_node)
        raise Exception(f"Unsupported text node type {text_node.text_type}")
    
    def split_nodes_delimiter(self, old_nodes, delimiter, text_type):
        output = []
        
        for node in old_nodes:
            if node.text_type is not text_type_text:
                output.append(node)
                continue
            splitted = node.text.split(delimiter)

            if len(splitted) % 2 == 0:
                raise Exception(f"Closing delimater {delimiter} not found in {node.text}.")
            
            for i in range(0, len(splitted)):
                if i % 2 != 0:
                   output.append(TextNode(splitted[i], text_type))
                elif splitted[i] != "":
                   output.append(TextNode(splitted[i], text_type_text))  
            continue

        return output
    
    def split_nodes_image(self, old_nodes):
        return self.__split_nodes(old_nodes, extract_markdown_images, lambda image: f"![{image[0]}]({image[1]})", text_type_image)
    
    def split_nodes_link(self, old_nodes):
        return self.__split_nodes(old_nodes, extract_markdown_links, lambda link: f"[{link[0]}]({link[1]})", text_type_link)
    
    def text_to_textnodes(self, text):
        base_node = TextNode(text, text_type_text)
        ans = [base_node]
        for type in base_node.text_type_delimeter:
            ans = self.split_nodes_delimiter(ans, base_node.text_type_delimeter[type], type)

        ans = self.split_nodes_image(ans)
        ans = self.split_nodes_link(ans)

        return ans
    
    def __split_nodes(self, old_nodes, extract_func, get_original_func, text_type):
        ans = []

        for node in old_nodes:
            items = extract_func(node.text)
            if len(items) < 1:
                ans.append(node)
                continue

            for item in items:
                original_text = get_original_func(item)
                splitted = node.text.split(original_text, 1)
                if splitted[0] != "":
                    ans.append(TextNode(splitted[0], text_type_text))
                ans.append(TextNode(item[0], text_type, item[1]))
                node.text = node.text.replace(original_text, "")
                node.text = node.text.replace(splitted[0], "")
            if node.text != "":
                ans.append(TextNode(node.text, text_type_text))
        return ans  



    