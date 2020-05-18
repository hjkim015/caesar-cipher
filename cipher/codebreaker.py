
from nltk.corpus import words
import numpy as np
import re

word_list = words.words()
message = '''Ovg fh ivgfim uli z nlnvmg gl Ozwb Olevozxv’h lyqvxgrlm dsrxs hgzgvw gszg gsv nzxsrmv xzm lmob wl dszg dv gvoo rg gl wl'''
#message = "ji he noem li gaiiag"
alphabet = "abcdefghijklmnopqrstuvwxyz" + "’"
punctuation = "?!.,"
sol_dict= {}
length_dict = {}


def create_length_dict():
#creates a dictionary that organizes English words based on their length
    for key in word_list:
        length = len(key)
        if length in length_dict:
            length_dict[length].append(key)
        else:
            length_dict[length] = [key]
    length_dict[1] = ["A", "a", "I", "i"]

def initialize_sol(message):
#sets each word in the message to a solution set equal to the word length
    message = message.lower()
    message_words = []
    word = ""
    i=1
    for symbol in message:
        if symbol in alphabet:
            word += symbol
            if i == len(message):
                message_words.append(word)
        else:
            message_words.append(word)
            word = ""
        i+=1
    for word in message_words:
    #matches each message word with potential solution list based on length
        length = len(word)
        sol_dict[word] = length_dict[length]

def pattern():
#removes solutions that don't fit duplicate pattern
    for word in sol_dict:
        print(word)
        find_duplicates(word)
        input()


            # for i in range(len(duplicates)):
            #     n = i+1
            #     word = word.replace(duplicates[i],str(n))
            #     print(word)


    index_positions = {}

def find_duplicates(word):
#finds the indices of all letters in word
    regexPattern = re.compile('[a-zA-Z0-9]')
    iteratorOfMatchObs = regexPattern.finditer(word)
    index_positions = {}

    for matchObj in iteratorOfMatchObs:
        index_positions[matchObj.group()] = index_positions.get(matchObj.group(), []) + [matchObj.start()]

    print(index_positions.items())

def codify(word,index_positions):
#turns the encoded words and all potential solutions into number codes
    zeros = word.replace(word, "0" * len(word))
    print(index_positions)


        #print(code)
    # for (key, value) in index_positions.items():
    #     if len(index_positions[key]) >= 2:
    #        ß print("indices of ", key , " is : ", index_positions[key])















create_length_dict()
initialize_sol(message)
pattern()
#find_duplicates("olevozxv’h")
#codify("nlnvmg", index_positions)
