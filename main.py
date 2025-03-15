frankenstein = "./books/frankenstein.txt"
words = ""

def get_book_text(book_path):
    with open(book_path) as f:
        book_text = f.read()
        return book_text
    
def main(book):
    book_text = get_book_text(book)
    words = book_text.split()
    print(f"{len(words)} words found in the document")

main(frankenstein)