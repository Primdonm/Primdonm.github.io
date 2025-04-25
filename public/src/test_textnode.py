import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.TEXT,"https://battle.net")
        node2 = TextNode("This is a text node", TextType.TEXT,"https://battle.net")
        self.assertEqual(node, node2)

    def test_eq_not_equal(self):
        node = TextNode("This is a text node", TextType.CODE)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()