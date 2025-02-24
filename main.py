from stats import word_count, char_count


def get_book_text(path_to_file):
    with open(path_to_file, 'r') as file:
        return file.read()

def main():
    file_content = get_book_text("books/frankenstein.txt")
    file_word_count = word_count(file_content)
    char_counts = char_count(file_content)
    print(f"{file_word_count} words found in the document")

    for char, count in char_counts.items():
        print(f"'{char}': {count}")


    




main()