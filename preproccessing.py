import os
import csv
import re

word_list_file = 'wordlist.csv'
dict_file = 'dictionary.txt'
word_list = []
dictionary_by_word_type = dict()

# Read word list into memory
with open(word_list_file, mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
    word = lines[0]
    if len(lines) == 3: # Skip the first line
      types = str.split(lines[2],' ') # split into an array by space delimiter
      # print(types)
      # For every type associated with that word, add it to a list in the dictionary at that key value
      for type in types:
        if type not in dictionary_by_word_type:
          # If this is the first time seeing this type, start an empty array there
          dictionary_by_word_type[type] = []
        dictionary_by_word_type[type].append(word)

# Main loop
for type in dictionary_by_word_type.keys():
  instances = len(dictionary_by_word_type[type])
  print(type + " " + str(instances))

# noun 1525
# adjective 308
# verb 800
# conjunction 3
# preposition 12
# adverb 50
# interjection 16
# pronoun 13
# idiom 94
# auxiliary 3