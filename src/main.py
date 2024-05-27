from blockutils import extract_title, markdown_to_html_node
from filesystemutils import copy_dir_content, read_file, save_file, get_all_files_paths

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    markdowns_paths = get_all_files_paths(dir_path_content, "md")
    for path in markdowns_paths:
        subPath = path.replace(dir_path_content, "").replace("md", "html")
        print(dest_dir_path + subPath)
        generate_page(path, template_path, dest_dir_path + subPath)
    
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    source_markdown = read_file(from_path)
    template = read_file(template_path)
    content = markdown_to_html_node(source_markdown).to_html()
    title = extract_title(source_markdown)
    output = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    save_file(dest_path, output, create_dir=True)

def main():
    copy_dir_content("./static", "./public")
    generate_pages_recursive("./content", "template.html", "./public")

if __name__ == "__main__":
    main()