import os
import shutil

from textnode import TextNode, TextType
from copystatic import copy_files_recursive
from gencontent import generate_page

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating page...")
    generate_page(
        os.path.join(dir_path_content, "index.md"),
        template_path,
        os.path.join(dir_path_public, "index.html"),
    )

main()
# def copy_static_files(static, public):
#     # First, delete the destination directory if it exists
#     if os.path.exists(public):
#         shutil.rmtree(public)
    
#     # Create the destination directory
#     os.mkdir(public)
    
#     # TODO: Add your recursive copying logic here
#     # Hint: You'll need to loop through all items in source_dir
#     # and handle files and directories differently
#     # Get all items in the source directory
#     for item in os.listdir(static):
#         # Create full paths
#         source_item = os.path.join(static, item)
#         dest_item = os.path.join(public, item)
        
#         # If it's a file, copy it
#         if os.path.isfile(source_item):
#             print(f"Copying file: {source_item} to {dest_item}")
#             shutil.copy(source_item, dest_item)
#         # If it's a directory, create it and recursively copy contents
#         else:
#             print(f"Creating directory: {dest_item}")
#             os.mkdir(dest_item)
#             # Here's the recursive call - we call the same function 
#             # but with the subdirectory paths
#             copy_static_files(source_item, dest_item)

# print("hello world")
# def main():
#     node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
#     print(node)
#     copy_static_files('static', 'public')

# if __name__ == "__main__":
    

