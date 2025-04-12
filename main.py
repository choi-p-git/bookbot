import sys

if len(sys.argv) < 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import word_counter  # Word_counter function in remote location
from stats import char_sort     # Char_sort functions in remote location

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
word_counter(sys.argv[1])
print("--------- Character Count -------")
char_sort(sys.argv[1])