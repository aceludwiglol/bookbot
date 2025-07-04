def get_num_words(text):

    words = text.split() # Count the number of words ina  text string.
    return len(words)

def get_character_counts(text):
    
    char_counts = {} #count the characters in the text

    for char in text:
        lowercase_char = char.lower() #Converts to lowercase to avoid duplicates

        #Adds to dictionary or adds to counter
        if lowercase_char in char_counts: 
            char_counts[lowercase_char] += 1
        else:
            char_counts[lowercase_char] = 1
        
    return char_counts

def sort_on(item):
    return item['num'] #Just a helper function for sorting

def get_sorted_char_list(char_counts):
    #converts dictionary to list of dictionaries
    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})
    
    #Sort by count DESC
    char_list.sort(reverse=True, key=sort_on)

    return char_list
    