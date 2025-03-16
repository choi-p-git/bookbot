frankenstein = "books/frankenstein.txt"   # set book location

# Word_counter function in remote location

from stats import word_counter
from stats import char_sort

print("============ BOOKBOT ============")
print(f"Analyzing book found at {frankenstein}...")
print("----------- Word Count ----------")
word_counter(frankenstein)
print("--------- Character Count -------")
char_sort(frankenstein)