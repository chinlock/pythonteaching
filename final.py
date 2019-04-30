## program can be improved to remove case sensitivties -- e.g. use string.lower()

STRIP_CHARS="?!.,;:"

def lines_count(text):
  return len(text)

def word_count(text):
  p = []
  for l in lines:
    words = l.strip().split()
    for w in words:
      k = w.strip(STRIP_CHARS)
      p.append(k)
  return p, len(p)

def count_appear(word, word_list):
  count=0
  for w in word_list:
    if w == word:
      count += 1
  return count

def lines_with_word(word, lines):
  lineNumbers = []
  for i in range(0, len(lines)):
    words = lines[i].strip().split()
    for w in words:
      k = w.strip(STRIP_CHARS)
      if k==word:
        lineNumbers.append(i)
  return lineNumbers

def lines_with_2words(word1, word2, lines):
  lineNumbers = []
  for i in range(0, len(lines)):
    words = lines[i].strip().split()
    linewords=[]
    for w in words:
      k = w.strip(STRIP_CHARS)
      linewords.append(k)
    if word1 in linewords and word2 in linewords:
      lineNumbers.append(i)
  return lineNumbers
    
### 
f = open("1342-0.txt", "r")
lines = f.readlines()
f.close()

num_lines = lines_count(lines)
word_list, num_words = word_count(lines)

print("num lines:", num_lines)
print("num words:", num_words)
#print(word_list[0:100])

w = input("Enter Search Word: ")
print(count_appear(w, word_list), "times")
print("lines:",lines_with_word(w, lines))

w1 = input("Enter 1st word:")
w2 = input("Enter 2nd word:")
print("lines:",lines_with_2words(w1, w2, lines))
