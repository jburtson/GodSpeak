import os
import csv

random_word_list = []
typed_word_list_dictionary = {}

# Read word list into memory
def read_random_word_list():
    word_list_file = 'dictionary.txt'
    with open(word_list_file, mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            random_word_list.append(lines[0])
            # print(lines[0])

def read_labeled_word_list():
    word_list_file = 'wordlist.csv'
    with open(word_list_file, mode ='r')as file:
        csvFile = csv.reader(file)
        types = lines[3]
        # TODO: Parse lines[3] for all word types, then add to dictionary for each type, array of words
        for lines in csvFile:
            typed_word_list_dictionary[types] = lines[0]
            print(lines[0])

# Get random int (inclusive) from a range. Uses random bytes.
def get_random_int(min_value, max_value):
    byte_length = max_value.bit_length() + 7 // 8
    random_bytes = os.urandom(byte_length)
    random_int = int.from_bytes(random_bytes, 'big') % (max_value - min_value + 1) + min_value
    return random_int

# Gets a random word from word list
def get_random_word():
    list_size = random_word_list.__len__()
    i = get_random_int(0, list_size-1)
    return random_word_list[i]

# Create a sentence of random words from word list, of specified number of words
def get_random_sentence(length):
    sentence = ""
    for n in range(length):
        sentence = sentence + get_random_word() + " "
    sentence = sentence[0].upper() + sentence[1:-1]
    punctuation = get_random_int(0,6)

    # Add random punctuation
    if (punctuation <= 3):
       sentence = sentence + '.'
    elif (punctuation <= 5):
       sentence = sentence + '?'
    elif (punctuation <= 6):
       sentence = sentence + '!'
    
    print(sentence)
    return sentence

# Main loop, prompts for new sentences.
print("Input anything to continue, x or q to exit.")
user_input = ""
while(user_input != "x" or user_input != "1"):
    sentence_length = get_random_int(8,18)
    get_random_sentence(sentence_length)
    user_input = input()