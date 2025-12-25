from stats import count_words, count_characters

def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
    return file_contents

def main():
  text = get_book_text("books/frankenstein.txt")
  print(f"Found {count_words(text)} total words")
  print(count_characters(text))

main()