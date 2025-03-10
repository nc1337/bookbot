import sys
from stats import get_character_freq, get_num_words, get_sorted_character_freq 
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    freq = get_character_freq(text)
    sorted_freq = get_sorted_character_freq(freq)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character, freq in sorted_freq.items():
        if character.isalpha():
            print(f"{character}: {freq}")
    print("============= END ===============")

main()
