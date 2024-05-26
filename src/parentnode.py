from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, children, tag = None, props = None):
        super().__init__(tag=tag, children=children, props=props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Tag cannot be empty")
        if self.children is None or len(self.children)<1:
            raise ValueError("Children cannot be empty for parent node")
        
        ans = ""
        for child in self.children:
            ans += child.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{ans}</{self.tag}>"