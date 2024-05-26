class HTMLNode:
    def __init__(self, tag = None, value = None, 
                 children = None, props = None):
        self.tag = tag
        self.value= value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if not self.props:
            return ""

        ans = ""

        for prop_name in self.props:
            ans += f" {prop_name}=\"{self.props[prop_name]}\""
        
        return ans
    
    def __repr__(self):
        return f"{self.tag}, {self.value}, {self.children} {self.props}"