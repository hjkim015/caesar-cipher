# credits for replace_string_function --> https://stackoverflow.com/questions/41752946/replacing-a-character-from-a-certain-index
# credits for find find_letter_indices function --> https://stackoverflow.com/questions/11122291/how-to-find-char-in-string-and-get-all-the-indexes
from nltk.corpus import words
import numpy as np
import re

word_bank = words.words()

#message = "ivgfim"
message = '''Ovg fh ivgfim uli z nlnvmg gl Ozwb lyqvxgrlm dsrxs hgzgvw gszg gsv nzxsrmv xzm lmob wl dszg dv gvoo rg gl wl'''
alphabet = "abcdefghijklmnopqrstuvwxyz"
alpha_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
contraction = " ' ’ "
punctuation = "?!.,"
sol_dict= {}
sol_letter_dict = {}
length_dict = {}

def initialize_length_dict():
#creates a dictionary that organizes English words based on their length
    for key in word_bank:
        length = len(key)
        if length in length_dict:
            length_dict[length].append(key)
        else:
            length_dict[length] = [key]
    length_dict[1] = ["a", "i"]

def initialize_sol(message):
#sets each word in the message to a solution set equal to the word length
    for sol in word_bank:
        sol.lower()

    message = message.lower()
    message_words = []
    message_letters = []
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
    #creates length_dict
        length = len(word)
        sol_dict[word] = length_dict[length]

    for letter in message:
        if letter in alphabet and letter not in message_letters:
            message_letters.append(letter)
    for letter in message_letters:
    #creates letter_dict
        sol_letter_dict[letter] = alpha_list
    for word in sol_dict:
    #modifies letter_dict to cater to one letter words
        if len(word) == 1:
            sol_letter_dict[word] = sol_dict[word]

def pattern():
#removes solutions that don't fit duplicate pattern
    for word in sol_dict:
        duplicates = []
        for letter in word:
            if word.count(letter) > 1 and letter not in duplicates:
                duplicates.append(letter)
        if len(duplicates) >= 1:
            code = codify(word)
            for sol in sol_dict[word]:
                test_code = codify(sol)
                if test_code != code:
                    sol_dict[word].remove(sol)

def find_indices(word):
#finds the index positions of every letter in the word
    index_positions = {}
    regexPattern = re.compile('[a-zA-Z0-9]')
    iteratorOfMatchObs = regexPattern.finditer(word)
    for matchObj in iteratorOfMatchObs:
        index_positions[matchObj.group()] = index_positions.get(matchObj.group(), []) + [matchObj.start()]
    return index_positions

def find_letter_indices(s, ch):
#finds the index position of a specific letter in a word
    indices = [i for i, ltr in enumerate(s) if ltr == ch]
    return indices

def codify(word):
#finds the indices of all letters in word then encodes them into numbers
    index_positions = find_indices(word)
    for key in list(index_positions.keys()):
    #Only look at duplicates
        if len(index_positions[key]) <= 1:
            index_positions.pop(key)
    code = ""
    zeros = word.replace(word, "0" * len(word))
    i = 0
    for letter in index_positions:
        key_value = index_positions[letter]
        for m in range(len(key_value)):
            n = i+1
            position = key_value[m]
            def replace_str_index(text,index=0,replacement=''):
                replacement = '%s%s%s'%(text[:index],replacement,text[index+1:])
                return replacement
            zeros = replace_str_index(zeros, position, str(n))
        i+=1

    index_positions.clear()
    return zeros

def one_letter():
    print(sol_letter_dict.keys())

    for key, values in sol_letter_dict.items():
        length = len(sol_letter_dict[key])
        for value in values:
            input()
            print("the value we are on for the key: ", key, "is: ", value)
            print("Before", length)
            test_dict = sol_dict.copy()
            test_letter = value
            encoded_letter = key
            print(sol_letter_dict[encoded_letter])
            for word in test_dict:
                input()
                if encoded_letter in word:
                    indices = find_letter_indices(word, encoded_letter)
                    print("indices for encoded letter", encoded_letter, "in the word: ", word, indices)
                    for sol in test_dict[word]:
                        input()
                        test_indices = find_letter_indices(sol, test_letter)
                        print("indices for test letter ", test_letter, "in potential sol: ", sol, test_indices)
                        if test_indices != indices:
                            print("potential solutions length is before: ", len(test_dict[word]))
                            test_dict[word].remove(sol)
                            print("potential solutions length after: ", len(test_dict[word]))
            if len(test_dict[word]) == 0:
                sol_letter_dict[encoded_letter].remove(test_letter)
                print("after", length)


    print(sol_letter_dict)




#set single letter to either "a" or "i"
#randomly assign cipher letters, if any of the words go empty, it can't word_bank
#test this like 25*25 times for every alphabet letter.
#testing one at a time.

#letter dict: key is message letter, key value is alphabet letter
#assign the letter, and go through every encoded word that has that letter
#if word bank empty eliminate.



initialize_length_dict()
initialize_sol(message)
pattern()
one_letter()
