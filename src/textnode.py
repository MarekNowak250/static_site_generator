text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, toComapre):
        return (self.text == toComapre.text 
            and self.text_type == toComapre.text_type
            and self.url == toComapre.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    text_type_delimeter = {
        text_type_bold: "**",
        text_type_italic: "*",
        text_type_code: "`",
    }