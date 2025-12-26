import sys
from stats import count_words, count_characters, chars_dict_to_sorted_list

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
    return file_contents

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {sys.argv[1]}...")
  print("----------- Word Count ----------")
  text = get_book_text(sys.argv[1])
  print(f"Found {count_words(text)} total words")
  
  print("--------- Character Count -------")
  char_info = count_characters(text)
  sorted_char_list = chars_dict_to_sorted_list(char_info)
  for char_stat in sorted_char_list:
    print(f"{char_stat["char"]}: {char_stat["num"]}")

main()