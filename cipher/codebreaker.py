# credits for replace_string_function --> https://stackoverflow.com/questions/41752946/replacing-a-character-from-a-certain-index




from nltk.corpus import words
import numpy as np
import re

word_list = words.words()
#message = '''Ovg fh ivgfim uli z nlnvmg gl Ozwb Olevozxv’h lyqvxgrlm dsrxs hgzgvw gszg gsv nzxsrmv xzm lmob wl dszg dv gvoo rg gl wl'''
message = "Olevozxv’h"
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
        input()
        print(word)
        duplicates = []
        for letter in word:
            if word.count(letter) > 1 and letter not in duplicates:
                duplicates.append(letter)
        if len(duplicates) >= 1:
            input()
            print("before", len(sol_dict[word]))
            code = codify(word)
            for sol in sol_dict[word]:
                test_code = codify(sol)
                print("code", code)
                print("test", test_code)
                print(sol)
                if test_code != code:
                    sol_dict[word].remove(sol)
                    if sol not in sol_dict[word]:
                        print("status: removed")
                    input()
            print("after", len(sol_dict[word]))


def codify(word):
#finds the indices of all letters in word then encodes
    index_positions = {}
    regexPattern = re.compile('[a-zA-Z0-9]')
    iteratorOfMatchObs = regexPattern.finditer(word)
    for matchObj in iteratorOfMatchObs:
        index_positions[matchObj.group()] = index_positions.get(matchObj.group(), []) + [matchObj.start()]
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





        #print(code)
    # for (key, value) in index_positions.items():
    #     if len(index_positions[key]) >= 2:
    #        ß print("indices of ", key , " is : ", index_positions[key])




create_length_dict()
initialize_sol(message)
pattern()
