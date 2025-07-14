def get_book_text(filepath):
    with open (filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    file_contents = get_book_text("books/frankenstein.txt")
    word_count = num_of_words(file_contents)
    print(f"{word_count} words found in the document")

def num_of_words(book_text):
    word_count = len(book_text.split())
    return word_count
    


    
main()
    

