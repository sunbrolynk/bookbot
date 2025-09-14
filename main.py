from stats import *
import sys

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path-to-book>")
	sys.exit(1)

word_count = get_num_words(sys.argv[1])
char_dict = char_count(sys.argv[1])
sorted_chars = sorted_list(char_dict)




print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")

print(f"Found {word_count} total words")

print("--------- Character Count -------")

for item in sorted_chars:
	ch = item["char"]
	if ch.isalpha():
		print(f"{ch}: {item['num']}")

print("============= END ===============")
