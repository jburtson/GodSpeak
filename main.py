import os
import csv

random_word_list = []
typed_word_list_dictionary = {}
adlib_sentence_list = []

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
        skipfirst = True
        for line in csvFile:
            # Skip first line
            if(skipfirst):
                skipfirst = False
                continue
            # TODO: Parse lines[3] for all word types, then add to dictionary for each type, array of words
            types = line[2].split(' ')
            word = line[0]
            for type in types:
                if typed_word_list_dictionary.get(type) is None:
                    typed_word_list_dictionary[type] = []
                typed_word_list_dictionary[type].append(word)
            # print(typed_word_list_dictionary[type])

def read_adlib_sentence_list():
    word_list_file = 'adlib.csv'
    with open(word_list_file, mode ='r')as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            adlib_sentence_list.append(lines[0])
            # print(lines[0])

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

def get_random_type_word(type):
    word_list = typed_word_list_dictionary[type]
    list_size = word_list.__len__()
    i = get_random_int(0, list_size-1)
    return word_list[i]

def does_type_exist(type):
    return typed_word_list_dictionary.__contains__(type)

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

def get_random_template():
    list_size = adlib_sentence_list.__len__()
    i = get_random_int(0, list_size-1)
    return adlib_sentence_list[i]

def get_random_template_sentence():
    sentence_template = get_random_template()
    sentence = ""
    for word in sentence_template.split(' '):
        # If special template word
        if word[0] == '$':
            # sentence += word[1:]
            type = word[1:]
            if does_type_exist(type):
                template_word = get_random_type_word(type)
                sentence += template_word + ' '
            else:
                match type:
                    case 'subject':
                        template_word = get_random_type_word("noun")
                        sentence += template_word + ' '
                    case 'new-subject':
                        template_word = get_random_type_word("noun")
                        sentence += template_word + ' '
                    case _:
                        print("No such thing as "+type)
        # Print whatever was in template
        else:
            sentence += word + ' '
    return sentence

read_random_word_list()
read_labeled_word_list()
read_adlib_sentence_list()
# Main loop, prompts for new sentences.
print("Input anything to continue, x or q to exit.")
user_input = " "
while(not user_input.startswith(tuple(['x','q']))):
    sentence_length = get_random_int(8,18)
    # get_random_sentence(sentence_length)
    print(get_random_template_sentence())
    user_input = input()