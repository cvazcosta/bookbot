def main ():
    text = get_text()

    number_of_words = count_words(text)

    char_dict = count_characters(text)
    #print(f"char_dict:{char_dict}")

    char_list = dict_to_list(char_dict)
    #print(f"char_list:{char_list}")

    char_list.sort(reverse=True, key=sort_on)
    #print(f"sorted_dict:{char_list}")

def sort_on(dict):
    return dict["num"]

def get_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    number_of_words = len(text.split())
    return number_of_words

def count_characters(text):
    character_dict = {}
    # passando todo o texto para lower case
    lowered_text = text.lower()
    # iterando em cada palavra de text
    word_list = lowered_text.split()

    for word in word_list:
        for character in word:
            if character.isalpha():
                if character in character_dict:
                    character_dict[character] += 1
                else:
                    character_dict[character] = 1
    #print(f"character_dict:{character_dict}")
    return character_dict

def dict_to_list(dict):
    char_list = []
    for char in dict:      
        char_dict = {}
        char_dict["char"] = char
        char_dict["num"] = dict[char]
        char_list.append(char_dict)  
    return char_list

main()