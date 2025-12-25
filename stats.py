def count_words(text):
  words = text.split()
  return len(words)

def count_characters(text):
  words_dictionary = {}

  for word in text.lower():
    if word in words_dictionary:
      words_dictionary[word] += 1
    else:
      words_dictionary[word] = 1
      
  return words_dictionary