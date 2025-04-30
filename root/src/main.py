import os
import shutil

from textnode import TextNode, TextType

def copy_static_files(static, public):
    # First, delete the destination directory if it exists
    if os.path.exists(public):
        shutil.rmtree(public)
    
    # Create the destination directory
    os.mkdir(public)
    
    # TODO: Add your recursive copying logic here
    # Hint: You'll need to loop through all items in source_dir
    # and handle files and directories differently
    # Get all items in the source directory
    for item in os.listdir(static):
        # Create full paths
        source_item = os.path.join(static, item)
        dest_item = os.path.join(public, item)
        
        # If it's a file, copy it
        if os.path.isfile(source_item):
            print(f"Copying file: {source_item} to {dest_item}")
            shutil.copy(source_item, dest_item)
        # If it's a directory, create it and recursively copy contents
        else:
            print(f"Creating directory: {dest_item}")
            os.mkdir(dest_item)
            # Here's the recursive call - we call the same function 
            # but with the subdirectory paths
            copy_static_files(source_item, dest_item)

print("hello world")
def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)
    copy_static_files('static', 'public')

if __name__ == "__main__":
    main()

