def get_book_text(path_to_file):
    with open(path_to_file, 'r') as file:
        return file.read()

def main():
    file_content = get_book_text("books/frankenstein.txt")
    print(file_content)


main()