import sys
from stats import get_num_words, get_character_counts, get_sorted_char_list

def get_book_text(filepath):

    # Reads contents and returns as a string
    with open(filepath, 'r', encoding ='utf-8') as file:
        return file.read()

def main():
    #check if correct number of arguments are provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    #gets the filepath from command line arguments
    filepath = sys.argv[1]

    #read book content
    book_content = get_book_text(filepath) #reads book

    #get statistics
    num_words = get_num_words(book_content)
    char_counts = get_character_counts(book_content)
    sorted_chars = get_sorted_char_list(char_counts)

    #Output
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    #Prints only alpha chars
    for char_data in sorted_chars:
        char = char_data["char"]
        count = char_data["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()


