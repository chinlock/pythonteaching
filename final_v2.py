## improved version, tidied up

STRIP_CHARS = '”?!.,;:(){}[]*#'    # chars to strip from a word
PRIDE_BOOK = "1342-0.txt"          # book: pride & prejudice 
WAR_BOOK = "2600-0.txt"            # book: war & peace

# cleans text, returns number of words, number of lines
# and the cleaned text
def clean_book(text):
  cleaned_book = list()  
  word_count = 0
  for l in text:  # go line by line
    cleaned_l = [w.strip(STRIP_CHARS).lower() for w in l.strip().split()] # list of cleaned words
    cleaned_book.append(cleaned_l) # append to list of cleaned lines to become cleaned book
    word_count += len(cleaned_l)
  return word_count, len(cleaned_book), cleaned_book

# count number of times a word occurs in cleaned_book
# and returns also the line numbers where the word occurs
def count_appear(word, cleaned_book):
  count = 0
  line_numbers = list()
  for index, line in enumerate(cleaned_book):
    if line.count(word) > 0:
      count += line.count(word)
      line_numbers.append(index+1)  # to make line numbers start from 1 instead of 0
  return count, line_numbers

# returns the list of linenumbers where word1 and word2 
# occurs in cleaned_book.  
def count_appear2(word1, word2, cleaned_book):
  line_numbers=[]
  for index, line in enumerate(cleaned_book):
    if line.count(word1) > 0 and line.count(word2) > 0:
      line_numbers.append(index+1)  # to make line numbers start from 1 instead of 0
  return len(line_numbers), line_numbers

def find_intersect_words(cleaned_book1, cleaned_book2, N=1):
  # create word maps for book1 and book2
  # each word map is a dict that counts how many times
  # a word occurs in the book e.g. { 'pride': 49, ... }
  word_map1 = dict()
  for l in cleaned_book1:
    for w in l:
      if w in word_map1:
        word_map1[w] += 1
      else:
        word_map1[w] = 1
  
  word_map2 = dict()
  for l in cleaned_book2:
    for w in l:
      if w in word_map2:
        word_map2[w] += 1
      else:
        word_map2[w] = 1

  ## get list of words that occur more than N times in 
  # each book and put them into sets

  word_set1 = set()
  word_set2 = set()
  for key, value in word_map1.items():
    if value >= N:
      word_set1.add(key)
  for key, value in word_map2.items():
    if value >= N:
      word_set2.add(key)

  # similar words are words that intersect
  return word_set1.intersection(word_set2)

###  main  ###

f1 = open(PRIDE_BOOK, mode="r", encoding='utf-8-sig') # to remove the BOM encoding at the beginning
book1 = f1.readlines()
f1.close()

num_words_book1, num_lines_book1, cleaned_book1 = clean_book(book1)
print(PRIDE_BOOK,"| word count:", num_words_book1,"| num lines:",num_lines_book1)
#print(book1[:50])

## check how many times a word appears in the book
## show list of line numbers the word appears
w = input("Enter a word:").lower()
n, linenumbers = count_appear(w, cleaned_book1)
print(n, "times in lines", linenumbers)

## show line numbers where 2 words appear
w1, w2 = input("Enter 2 words:").lower().split()
n, linenumbers = count_appear2(w1, w2, cleaned_book1)
print(n, "times in lines", linenumbers)

# open and read second book
f2 = open(WAR_BOOK, mode="r", encoding='utf-8-sig')
book2 = f2.readlines()
f2.close()
num_words_book2, num_lines_book2, cleaned_book2 = clean_book(book2)

#  Get words that occurs in both books at least N times
N = int(input("Enter N (word occurences):"))
intersect_list = find_intersect_words(cleaned_book1, cleaned_book2, N)
print("Words in both books that occurs >= {} times:".format(N), intersect_list)

### end ###