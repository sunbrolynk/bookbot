def get_book_text(filepath):
	file_contents = ""
	with open(filepath) as f:
		file_contents += f.read()
	return file_contents



def get_num_words(filepath):
	book_string = get_book_text(filepath)
	split_strings = book_string.split()
	word_count = 0
	for string in split_strings:
		word_count += 1
	return word_count


def char_count(filepath):
	book_string = get_book_text(filepath)
	lower_b_string = book_string.lower()
	char_count = {}
	for char in lower_b_string:
		if char not in char_count:
			char_count[char] = 1
		else:
			char_count[char] += 1

	return char_count



def sort_on(items):
	return items["num"]



def sorted_list(char_count):
	sorted_list = []
	for key,value in char_count.items():
		sorted_list.append({"char":key, "num": value})

	sorted_list.sort(reverse=True, key=sort_on)


	return sorted_list

def list_to_string(sorted_list):
	result_string = ""
	for item in sorted_list:
		if item['char'].isalpha():
			result_string += f"{item['char']} : {item['num']}\n"
	return result_string