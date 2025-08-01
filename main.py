import sys
from stats import get_num_words
from stats import get_character_count
from stats import sort_character_count
# main.py
# This script reads the contents of a text file and prints it to the console.
# It is designed to read a book text file located in the "books" directory.
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    sorted_character_count = []
    num_words_in_book = get_num_words(get_book_text(filepath))
    characters_in_book = get_character_count(get_book_text(filepath))
    sorted_character_count = sort_character_count(characters_in_book)
    # Print the results to the console
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words_in_book} total words")
    print("--------- Character Count -------")
    for character in sorted_character_count:
        if character["char"].isalpha():
            print(f"{character['char']}: {character['num']}")
    print("============= END ===============")
# This function reads the contents of a text file and returns it as a string.
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents=f.read()
    return file_contents
main()