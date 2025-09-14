from stats import *

word_count = get_num_words("books/frankenstein.txt")
char_dict = char_count("books/frankenstein.txt")
sorted_chars = sorted_list(char_dict)
chars_string = list_to_string(sorted_chars)




print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")

print(f"Found {word_count} total words")

print("--------- Character Count -------")

print(chars_string)

print("============= END ===============")