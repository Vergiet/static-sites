import os

from extract_header import extract_title
from markdown_blocks import markdown_to_html_node

def read_file(file):
    filepath = os.path.abspath(file)
    with open(filepath) as filepath:
        content = filepath.read()
        return content

def write_file(file, content):
    with open(os.path.abspath(file), "w") as f:
        f.write(content)

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using template {template_path} using basepath {basepath}")
    markdown = read_file(from_path)
    title = extract_title(markdown)
    html = (markdown_to_html_node(markdown)).to_html()

    template = read_file(template_path)
    render = template.replace("{{ Title }}", title)
    render = render.replace("{{ Content }}", html)
    render = render.replace('href="/', f'href="{basepath}')
    render = render.replace('src="/', f'src="{basepath}')

    if not os.path.exists(os.path.dirname(dest_path)):
        os.mkdir(os.path.dirname(dest_path))

    write_file(dest_path, render)



    print(render)


def generate_files_recusive(source_dir_path, template_path, dest_dir_path, basepath):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for filename in os.listdir(source_dir_path):
        from_path = os.path.join(source_dir_path, filename)
        dest_path = os.path.join(dest_dir_path, filename).replace(".md", ".html")


        if os.path.isfile(from_path):
            print(f" * {from_path} -> {dest_path}")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_files_recusive(from_path, template_path, dest_path, basepath)
