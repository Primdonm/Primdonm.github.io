from textnode import TextNode, TextType

print("hello world")
def main():
    node = TextNode("This is a text node", TextType.Bold, "https://www.boot.dev")
    print(node)

if __name__ == "__main__":
    main()
