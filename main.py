from stats import get_num_words
from stats import get_num_characters
from stats import sort_characters


def print_report(word_count, characters):
    print('============ BOOKBOT ============\n'
    'Analyzing book found at books/frankenstein.txt...\n'
    '----------- Word Count ----------\n')
    print(f'Found {word_count} total words\n')
    print('----------- Character Count ----------\n')
    for char in characters:
        print(f'{char[0]}: {char[1]}')

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    word_count = get_num_words(path_to_file)
    characters = get_num_characters(path_to_file)
    sorted_characters = sort_characters(characters)
    print_report(word_count, sorted_characters)

if __name__ == "__main__":
    main()