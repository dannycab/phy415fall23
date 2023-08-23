### Alia's notes to self on how to use jupyter books

When making a new .ipynb:

1. Add it to the _toc.yml table of contents file


When updating the book:

1. Save all changes to files
2. cd to folder 1 **beneath** the folder of the book and run `jupyter-book build --all book_name`. Drop the -all to just build new things.
3. push the changes on the main branch of the repo
4. cd to the book's folder and run `ghp-import -n -p -f _build/html`
