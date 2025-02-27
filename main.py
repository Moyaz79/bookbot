import sys
from stats import word_count, char_count, sorting



def get_book_text(path_to_file):
    with open(path_to_file, 'r') as file:
        return file.read()

def main():
    file_content = get_book_text(sys.argv[1])
    file_word_count = word_count(file_content)
    char_counts = char_count(file_content)
    sort_on = sorted(char_counts.items(), key=sorting, reverse=True)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print("Analyzing book found at book/frankenstein.txt...")
    print("----------- Word Count -----------")
    print(f"Found {file_word_count} total words")
    print("---------- Character Count ----------")
    for char, count in sort_on:
        print(f"{char}: {count}")
    print("============ END =============")



    




main()