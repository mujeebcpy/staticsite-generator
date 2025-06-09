from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main() -> None:
    text_node: TextNode = TextNode("This is some anchor text", TextType.LINK , "https://www.boot.dev")
    print(text_node)
    htmlnode = HTMLNode(props={"style":"color:red;"})
    print(htmlnode)


main()

