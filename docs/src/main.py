import os
import shutil
import sys

from textnode import TextNode, TextType
from copystatic import copy_files_recursive
from gencontent import generate_pages_recursive

basepath = "/"
repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


dir_path_static = os.path.join(repo_root, "static")
dir_path_public = os.path.join(repo_root, "docs")
dir_path_content = os.path.join(repo_root, "content")
template_path = os.path.join(repo_root, "template.html")


if len(sys.argv) > 1:
    basepath = sys.argv[1]

def main():
    print("Deleting docs directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)

    print("Creating .nojekyll file...")
    open(os.path.join(dir_path_public, ".nojekyll"), "w").close()

   # generate_pages_recursive(content_dir, template_dir, output_dir, basepath)


main()