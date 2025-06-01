# This function returns the number of words in a given text
def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return num_words

# This function returns the number of times each character, (including symbols and spaces), appears in the string.
def get_count_of_each_character(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Sort key
def sort_on(dict):
    return dict["num"]

# This function returns a sorted list of each character in the text
def sorted_list_of_each_char(dict_of_char):
    mylist = []
    for k in dict_of_char:
        mylist.append({"char": k, "num": dict_of_char[k]})
    mylist.sort(reverse=True, key=sort_on)
    return mylist