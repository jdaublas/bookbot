def character_count(text):
    char_dict = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in char_dict:
            char_dict[lowered_char] += 1
        else: 
            char_dict[lowered_char] = 1
    return char_dict

def count_words(str):
    words = str.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read().strip()    
    word_count = count_words(file_contents)
    char_counts = character_count(file_contents)
    print("Number of spaces found:", file_contents.count(' '))
    print(char_counts)
    
    
    
if __name__ == "__main__":
    main()


    

