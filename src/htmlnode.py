


class HTMLNode():
    def __init__(self, tag, value, children, props):
        self.tag = tag  # A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
                        # An HTMLNode without a tag will just render as raw text
        self.value = value  # A string representing the value of the HTML tag (e.g. the text inside a paragraph)
                            # An HTMLNode without a value will be assumed to have children
        self.children = children    # A list of HTMLNode objects representing the children of this node
                                    # An HTMLNode without children will be assumed to have a value
        self.props = props  # A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
                            # An HTMLNode without props simply won't have any attributes
    def to_html(self):
        raise NotImplementedError


    def props_to_html(self):
        html_props = []
        for key in self.props:
            html_props.append(f'{key}="{self.props[key]}"')

        return " "+" ".join(html_props)

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other):
        return (
            self.tag == other.tag and
            self.value == other.value and
            self.children == other.children and
            self.props == other.props
        )

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=""):
        super().__init__(tag, value, None, props)
        # if not value:
        #     raise ValueError('value may not be empty')

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

    def to_html(self):
        if self.tag == None:
            string = f'{self.value}'
        elif self.tag == "p":
            string = f'<p>{self.value}</p>'
        elif self.tag == "b":
            string = f'<b>{self.value}</b>'
        elif self.tag == "i":
            string = f'<i>{self.value}</i>'
        elif self.tag == "a":
            string = f'<a {self.props_to_html}>{self.value}</a>'
        else:
            raise NotImplementedError
        return string

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=""):
        super().__init__(tag, None, children, props)

    def to_html(self):
        child_strings = ""
        if not self.tag:
            raise ValueError("object must have a tag")
        for child in self.children:
            if not child.value:
                raise ValueError("Children must have value")
            else:
                child_strings = f"{child_strings}{child.to_html()}"

        return f"<{self.tag}>{child_strings}</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
