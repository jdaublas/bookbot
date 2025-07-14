def get_num_words(book_text):
    word_count = len(book_text.split())
    return word_count

def count_characters(characters):
    character_count = {}
    for i in range(len(characters.lower())):
        current_char = characters[i].lower()
        if current_char in character_count:
         character_count[current_char] = character_count[current_char] + 1
        else:
           character_count[current_char] = 1
    return character_count


