from stats import get_num_words
from stats import count_characters

def get_book_text(filepath):
    with open (filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    file_contents = get_book_text("books/frankenstein.txt")
    word_count = get_num_words(file_contents)
    character_counts = count_characters(file_contents)
    print(f"{word_count} words found in the document")
    print(character_counts)

def get_num_words(book_text):
    word_count = len(book_text.split())
    return word_count

    


    
main()
    

