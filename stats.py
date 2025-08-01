# This function counts the number of words in a given text.
# It splits the text into words and returns the count.
def get_num_words(book_text):
    words = book_text.split()
    return len(words)
# This function counts the number of characters in a given text.
# It returns a dictionary with character counts.
def get_character_count(book_text):
    characters_dict = {}
    for char in book_text:
        char = char.lower()
        if char not in characters_dict:
            characters_dict[char] = 0
        # Increment the count for the character
        characters_dict[char] += 1
    return characters_dict
# This function is used to sort the character count dictionary.
# It is used as a key function for sorting.
def sort_on(items):
   return items["num"]
# This function sorts the character count dictionary by the number of occurrences.
def sort_character_count(characters_dict):
    # Convert the dictionary to a list of dictionaries for sorting.
    sorted_dict_list = []
    for character in characters_dict:
        dict_item = {}
        dict_item["char"] = character
        dict_item["num"] = characters_dict[character]
        sorted_dict_list.append(dict_item)
    return sorted(sorted_dict_list, reverse=True, key=sort_on)
