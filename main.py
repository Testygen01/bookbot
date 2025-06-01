from stats import get_num_words, get_count_of_each_character, sorted_list_of_each_char
import sys

# This function returns the content of a file as string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

# Main function to execute the code
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # exit if no file path is provided

    # get filepath from command line
    filepath = sys.argv[1]

    # print file contents
    file_contents = get_book_text(filepath)

    # Report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    # print number of words in the text
    print("------------ Word Count ------------")
    num_words = get_num_words(file_contents)
    print(f"Found {num_words} total words")

    # returns one big dictionary of all the characters and their count
    print("------------ Character Count ------------")
    char_dict = get_count_of_each_character(file_contents)

    # returns a sorted list of character dictionary and their number of occurrence
    sorted_dict_char_list = sorted_list_of_each_char(char_dict)
    for dict in sorted_dict_char_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    
    print("============ END ============")

main()