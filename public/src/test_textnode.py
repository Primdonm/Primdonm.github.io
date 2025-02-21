import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.Bold)
        node2 = TextNode("This is a text node", TextType.Bold)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.Normal,"https://battle.net")
        node2 = TextNode("This is a text node", TextType.Normal,"https://battle.net")
        self.assertEqual(node, node2)

    def test_eq_not_equal(self):
        node = TextNode("This is a text node", TextType.Code)
        node2 = TextNode("This is a text node", TextType.Normal)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()