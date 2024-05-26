import re


markdown_block_delimeter = {
        heading_one: "#",
        text_type_italic: "###",
        text_type_code: "",
    }

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def markdown_to_blocks(markdown):
    ans = []
    currItem = []

    for item in markdown.split("\n"):
        if item != "":
            currItem.append(item.strip())
        elif currItem != []:
            ans.append(currItem)
            currItem = []
    if currItem != []:
        ans.append(currItem)

    return ans


