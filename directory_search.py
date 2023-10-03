import os
import json
import re

def find_notebooks_and_md_with_url(directory, url):
    # Create a regex pattern to search for the URL
    pattern = re.compile(r'\b' + re.escape(url) + r'\b')
    
    # List to store the filenames containing the URL
    filenames_with_url = []

    # Walk through all files in the directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Full path to the file
            filepath = os.path.join(root, file)
            
            # Check if file is a Jupyter notebook or markdown file
            if file.endswith(".ipynb") or file.endswith(".md"):
                # Read the file
                with open(filepath, 'r', encoding='utf-8') as f:
                    try:
                        # Check the file type and extract relevant content
                        if file.endswith(".ipynb"):
                            # Parse JSON content of Jupyter notebooks
                            content = json.load(f)
                            # Extract all text from the notebook cells
                            text_content = ''.join([
                                ''.join(cell['source']) for cell in content['cells'] if cell['cell_type'] == 'markdown'
                            ])
                        else: # .md file
                            # Directly read the text content of markdown files
                            text_content = f.read()
                        
                        # Search for the URL within the text content
                        if pattern.search(text_content):
                            filenames_with_url.append(filepath)
                    except Exception as e:
                        print(f"Error reading {filepath}: {str(e)}")
    
    return filenames_with_url


# Specify the directory to search and the URL to find
directory_to_search = './'
url_to_find = 'inv.tux.pizza'

# Execute the function
filenames = find_notebooks_and_md_with_url(directory_to_search, url_to_find)

# Output the results
if filenames:
    print(f"The following files contain the URL '{url_to_find}':")
    for filename in filenames:
        print(f"- {filename}")
else:
    print(f"No files containing the URL '{url_to_find}' were found in '{directory_to_search}'.")
