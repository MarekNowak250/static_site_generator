from leafnode import LeafNode
from parentnode import ParentNode
from textnodeutils import TextNodeUtils

block_type_heading = "heading",
block_type_paragraph = "paragraph",
block_type_code = "code",
block_type_quote = "quote",
block_type_unordered_list = "unordered_list",
block_type_ordered_list = "ordered_list",


def extract_content(text):
    utils = TextNodeUtils()
    nodes = utils.text_to_textnodes(text)
    content = ""
    for node in nodes:
        content += utils.text_node_to_html_node(node).to_html()
    return content

def convert_heading_to_html(block):
    splitted = block.split(" ", 1)
    return LeafNode(tag=f"h{len(splitted[0])}", value=extract_content(splitted[1]))

def convert_quote_to_html(block):
    return LeafNode(tag="blackquote", value=block.strip(">"))

def convert_code_to_html(block):
    leaf = LeafNode(tag="code", value=extract_content(block.strip("```")))
    return ParentNode(tag="pre", children=[leaf])

def convert_paragraph_to_html(block):
    return LeafNode(tag="p", value=extract_content(block))

def convert_ordered_list_to_html(block):
    lines = block.split("\n")
    children = []
    for line in lines:
        children.append(LeafNode(tag="li", value=extract_content(line[3:])))

    return ParentNode(tag="ol", children=children) 

def convert_unordered_list_to_html(block):
    lines = block.split("\n")
    children = []
    for line in lines:
        children.append(LeafNode(tag="li", value=extract_content(line[2:])))
    return ParentNode(tag="ul", children=children) 

block_to_html_node = {
    block_type_heading: convert_heading_to_html,
    block_type_paragraph: convert_paragraph_to_html,
    block_type_code: convert_code_to_html,
    block_type_quote: convert_quote_to_html,
    block_type_unordered_list: convert_unordered_list_to_html,
    block_type_ordered_list: convert_ordered_list_to_html,
}

def markdown_to_blocks(markdown):
    ans = []
    currItem = []

    for item in markdown.split("\n\n"):
        if item != "":
            currItem.append(item.strip())
        elif currItem != []:
            ans.extend(currItem)
            currItem = []
    if currItem != []:
        ans.extend(currItem)
        
    return ans

def block_to_block_type(markdown):
    if markdown.startswith("#"):
        splitted = markdown.split(" ", 1)
        if len(splitted) > 1 and len(splitted[0]) < 7 and splitted[0].replace("#", "") == "":
            return block_type_heading
    if markdown.startswith("```") and markdown.endswith('```'):
        return block_type_code
    if markdown.startswith(">"):
        splitted = markdown.split("\n")
        if __all_lines_stars_with(splitted, ">"):
            return block_type_quote
    if markdown.startswith("* ") or markdown.startswith("- "):
        splitted = markdown.split("\n")
        if __all_lines_stars_with(splitted, "* ") or __all_lines_stars_with(splitted, "- "):
            return block_type_unordered_list
    if markdown.startswith("1. "):
        num = 0
        match = True
        splitted = markdown.split("\n")
        for line in splitted:
            num +=1
            if not line.startswith(f"{num}. "):
                match = False
                break
        if match:
            return block_type_ordered_list

    return block_type_paragraph

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        type = block_to_block_type(block)
        if type == block_type_heading:
            splitted = block.split(" ", 1)
            if splitted[0] == "#":
                return splitted[1]
    raise Exception("No title (#) in a markdown file")

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    
    for block in blocks:
        type = block_to_block_type(block)
        children.append(block_to_html_node[type](block))
    
    return ParentNode(tag="div", children=children)

def __all_lines_stars_with(lines, characters):
    for line in lines:
        if not line.startswith(characters):
            return False
    return True        
