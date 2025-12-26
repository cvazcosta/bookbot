def count_words(text):
  words = text.split()
  return len(words)

def count_characters(text):
  char_counts = {}
  for char in text.lower():
    if char in char_counts:
      char_counts[char] += 1
    else:
      char_counts[char] = 1      
  return char_counts

def sort_on(char_info):
  return char_info["num"]

def chars_dict_to_sorted_list(char_counts):
  sorted_char_list = []
  for char in char_counts:
    if char.isalpha():
      char_info = {}
      char_info["char"] = char
      char_info["num"] = char_counts[char]
      sorted_char_list.append(char_info)
  sorted_char_list.sort(reverse=True, key=sort_on)
  return sorted_char_list