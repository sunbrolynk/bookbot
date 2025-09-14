from stats import *

word_count = get_num_words("books/frankenstein.txt")
char_dict = char_count("books/frankenstein.txt")
sorted_chars = sorted_list(char_dict)




print("============ BOOKBOT ============")
print("Analyzing book found at books/frankenstein.txt...")
print("----------- Word Count ----------")

print(f"Found {word_count} total words")

print("--------- Character Count -------")

for item in sorted_chars:
	ch = item["char"]
	if ch.isalpha():
		print(f"{ch}: {item['num']}")

print("============= END ===============")
