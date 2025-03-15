words = ""  # Set words as empty string
char_list = {"a" : 0, "b" : 0, "c" : 0, "d" : 0, "e" : 0, "f" : 0, "g" : 0, "h" : 0, "i" : 0, "j" : 0, "k" :0, "l" : 0, "m" :0, "n" : 0, "p" : 0, "q" : 0, "r" : 0, "s" : 0,
              "t" : 0, "u" : 0, "v" : 0, "w" : 0, "x" : 0, "y" : 0, "z" : 0}

# Word Counter Function

def word_counter(book):
    book_text = get_book_text(book)  # Retrieving text from get_book_text function
    words = book_text.split()        # Converting text string to word strings
    print(f"{len(words)} words found in the document")

# Character Counter Function

def char_counter(book):
    book_text = get_book_text(book)  # Retrieving text from get_book_text function
    characters = book_text.lower()
    for c in characters:
        if c in char_list:
            char_list[c] = char_list[c]+1
        else:
            char_list[c] = 1
    print(char_list)

# Characters to Dictionary Function





# Book Retrieval Function

def get_book_text(book_path):   # Secondary function call from main. main() > book > book_path
    with open(book_path) as f:  # Opening file path and use data as f
        book_text = f.read()    # set book_text as data read from file - output as string
        return book_text        # string value returned
    
