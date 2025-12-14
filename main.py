import os
import csv

# word_list_file = 'wordlist.csv'
word_list_file = 'dictionary.txt'
word_list = []
# Read word list into memory
with open(word_list_file, mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
    word_list.append(lines[0])
    # print(lines[0])


def get_random_int(min_value, max_value):
    byte_length = max_value.bit_length() + 7 // 8
    random_bytes = os.urandom(byte_length)
    random_int = int.from_bytes(random_bytes, 'big') % (max_value - min_value + 1) + min_value
    return random_int

def get_random_word():
    list_size = word_list.__len__()
    i = get_random_int(0, list_size-1)
    return word_list[i]

sentence_length = 20
sentence = ""
for n in range(sentence_length):
    sentence = sentence + get_random_word() + " "
print(sentence)