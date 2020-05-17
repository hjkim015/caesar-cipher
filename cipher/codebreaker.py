
from nltk.corpus import words
import numpy as np
word_list = words.words()
#word_list = ["A", "a", "aa", "aal", "aalii", "aam", "Aani", "b", "sdfg"]

message = '''Ovg fh ivgfim uli z nlnvmg gl Ozwb Olevozxv’h lyqvxgrlm dsrxs hgzgvw gszg gsv nzxsrmv xzm lmob wl dszg dv gvoo rg gl wl'''
#message = "ji he noem li gaiiag"
alphabet = "abcdefghijklmnopqrstuvwxyz" + "’"
punctuation = "?!.,"
sol_dict= {}
length_dict = {}

def create_length_dict():
#creates a dictionary that organizes English words based on their length
    for key in word_list:
    #goes through every English word and finds their length
        length = len(key)
        if length in length_dict:
        #if the word length is already in the new dict, just add the word
            length_dict[length].append(key)
        else:
        #otherwise, create another key value pair
            length_dict[length] = [key]
    length_dict[1] = ["A", "a", "I", "i"]

def initialize_sol(message):
    #sets each word in the message to a solution set equal to the word length
    message = message.lower()
    print(message)
    message_words = []
    word = ""
    i=1
    for symbol in message:
    #sort into a list of words in the message instead of letters
        if symbol in alphabet:
            word += symbol
            if i == len(message):
                #gets the very last word since it doesn't end with a space
                message_words.append(word)
        else:
            message_words.append(word)
            word = ""
        i+=1
    #print("list", message_words)
    for word in message_words:
    #matches each message word with potential solution list based on length
        #input()
        #print(word)
        length = len(word)
        sol_dict[word] = length_dict[length]
        #remember this will get rid of duplicates
        #print(sol_dict.keys())


def pattern():
#this function will go through
    for word in sol_dict:

        letter_freq = {}
        letter_uni_loc = {}

        for letter in word:
        #creates dictionary showing frequency of each letter in word
            if letter in letter_freq:
                letter_freq[letter] += 1
            else:
                letter_freq[letter] = 1

        for letter in list(letter_freq.keys()):
        #creates dict recording unique position of replicated letters
            replicate = []
            if letter_freq[letter] >= 2:
                for index in range(len(word)):
                    if word[index] == letter:
                        replicate.append(index)
                    else:
                        pass
                letter_uni_loc[letter] = replicate



        if len(letter_uni_loc) >= 1:
            print("final", word, letter, letter_uni_loc)
        else:
            pass








#Next steps:
    #looking for similar symbols?
    #



create_length_dict()
initialize_sol(message)
pattern()
