words = ""  # Set words as empty string
char_list = {"a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0, "i" : 0, "j" : 0, "k" :0, "l" : 0, "m" :0, "n" : 0, "p" : 0, "q" : 0, "r" : 0, "s" : 0,
              "t" : 0, "u" : 0, "v" : 0, "w" : 0, "x" : 0, "y" : 0, "z" : 0}
dict_list = []
# Word Counter Function

def word_counter(book):
    book_text = get_book_text(book)  # Retrieving text from get_book_text function
    words = book_text.split()        # Converting text string to word strings
    print(f"Found {len(words)} total words")

# Character Counter Function

def char_counter(book):
    book_text = get_book_text(book)         # Retrieving text from get_book_text function
    characters = book_text.lower()          # Converting text to lowercase
    for c in characters:                    # Iterating character in string
        if c in char_list:                  # Determining if character exist in dictionary
            char_list[c] = char_list[c]+1   # Add 1 to existing count
        else:
            char_list[c] = 1                # Character not in dictionary, set character as key and value to 1
    return char_list                        # Return dictionary

# Character Dictionary Sorting Function

def char_sort(book):
    unsorted_list = char_counter(book)                      # Acquire character dictionary from Character Counter Function
    for char, count in unsorted_list.items():               # Iterating key:value pair to create new list of 2 key dictionary
        temp_dict = {"character" : char, "count" : count}   # Setting "String" key to str / int values
        dict_list.append (temp_dict)                        # Appending each temp dictionary to list
    dict_list.sort(reverse=True, key=lambda x: x["count"])  # Sorting list by x: x["count"] through special key=lambda function in reverse
    for item in dict_list:                                  # Iterating each dictionary
        if item["character"].isalpha():                     # Determin if key "character" for dictionary is alphabetical character
            print (f"{item["character"]}: {item["count"]}") # Print as f-string
        else:
            continue                                        # Skip function


# Book Retrieval Function

def get_book_text(book_path):   # Secondary function call from main. main() > book > book_path
    with open(book_path) as f:  # Opening file path and use data as f
        book_text = f.read()    # set book_text as data read from file - output as string
        return book_text        # string value returned
    
