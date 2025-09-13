from stats import get_book_text, get_num_words, char_count, sorted_list

word_count = get_num_words("books/frankenstein.txt")
char_dict = char_count("books/frankenstein.txt")
sorted_chars = sorted_list(char_dict)





print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")

print(f"Found {word_count} total words")

print("--------- Character Count -------")



print("============= END ===============")
