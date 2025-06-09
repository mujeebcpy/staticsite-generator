import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_textnoteq(self):
        node1 = TextNode("This is a text node", TextType.ITALIC, "https://ibcomputing.com")
        node2 = TextNode("This is another text node", TextType.ITALIC, "https://ibcomputing.com")
        self.assertNotEqual(node1, node2)


    def test_urlnoteq(self) :
        node1 = TextNode("This is a text node", TextType.ITALIC, "https://ibcomputing.com")
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_texttypenoteq(self):
        node1 = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.ITALIC, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual("TextNode(This is a text node, text, https://www.boot.dev)", repr(node))

 
if __name__ == "__main__":
    unittest.main()
