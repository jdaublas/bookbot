def character_count(text):
    char_dict = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char.isalpha(): 
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
        file_contents = f.read()    
    word_count = count_words(file_contents)
    char_counts = character_count(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():  
            char_list.append({"char": char, "count": count})
    char_list.sort(reverse=True, key=lambda x: x["count"])
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['count']} times")
    print("--- End report ---")
      
if __name__ == "__main__":
    main()


    

