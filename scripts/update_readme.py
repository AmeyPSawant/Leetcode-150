import os
from urllib.parse import quote

# Paths
PROBLEMS_DIR = "Problems"
MAIN_README = "README.md"

def generate_problem_links():
    """Generate a hierarchical list of problem solutions links with relative URLs."""
    problem_links = []
    
    for problem_name in sorted(os.listdir(PROBLEMS_DIR)):
        problem_path = os.path.join(PROBLEMS_DIR, problem_name)
        if os.path.isdir(problem_path):
            # Get all .md and .txt files in the course directory
            files = [f for f in os.listdir(problem_path) if f.endswith((".md", ".txt"))]
            
            if files:
                # Generate the relative URL for the course directory
                problem_dir_path = os.path.join(PROBLEMS_DIR, problem_name).replace("\\", "/")
                # URL-encode the directory path
                encoded_dir_path = quote(problem_dir_path)
                # Ensure the path starts with ./
                problem_dir_url = f"./{encoded_dir_path}"
                # Add the course name as main list item with link to directory
                problem_links.append(f"* [{problem_name}]({problem_dir_url})")
                
                # Add each file as a sub-item
                for file_name in sorted(files):
                    file_path = os.path.join(problem_path, file_name)
                    
                    if file_name.endswith(".md"):
                        # For .md files, link directly to the file
                        relative_path = os.path.join(PROBLEMS_DIR, problem_name, file_name).replace("\\", "/")
                        encoded_path = quote(relative_path)
                        relative_url = f"./{encoded_path}"
                        file_display_name = file_name.replace(".md", "")
                        problem_links.append(f"   * [{file_display_name}]({relative_url})")
                    
                    elif file_name.endswith(".txt"):
                        # For .txt files, read the content and use it as a link
                        try:
                            with open(file_path, "r", encoding="utf-8") as txt_file:
                                content = txt_file.read().strip()
                                
                            if content:
                                # Use the content as the link URL
                                file_display_name = file_name.replace(".txt", "")
                                problem_links.append(f"   * <a href=\"{content}\" target=\"_blank\">{file_display_name}</a>")

                            else:
                                # If file is empty, just show the filename without a link
                                file_display_name = file_name.replace(".txt", "")
                                problem_links.append(f"   * {file_display_name} (empty file)")
                                
                        except Exception as e:
                            # If there's an error reading the file, show an error message
                            file_display_name = file_name.replace(".txt", "")
                            problem_links.append(f"   * {file_display_name} (error reading file: {e})")
    
    return problem_links

def update_main_readme(problem_links):
    """Update the main README.md file with the list of problem links."""
    with open(MAIN_README, "w", encoding="utf-8") as file:
        file.write("# Leetcode-150\n\n")
        file.write("Saving all my solutions to the problems solved\n\n")
        file.write("\n".join(problem_links))
        file.write("\n")

if __name__ == "__main__":
    # Generate problem links
    problem_links = generate_problem_links()
    print("Generated problem links:", problem_links)  # Debug statement
    
    # Update the main README.md
    update_main_readme(problem_links)
    
    print("README.md updated successfully!")