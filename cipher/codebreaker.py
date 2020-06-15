# credits for replace_string_function --> https://stackoverflow.com/questions/41752946/replacing-a-character-from-a-certain-index
# credits for find find_letter_indices function --> https://stackoverflow.com/questions/11122291/how-to-find-char-in-string-and-get-all-the-indexes
from nltk.corpus import words
import numpy as np
import string
import re

english_words = words.words()
message = '''Ovg fh ivgfim uli z nlnvmg gl Ozwb lyqvxgrlm dsrxs hgzgvw gszg gsv nzxsrmv xzm lmob wl dszg dv gvoo rg gl wl'''
alphabet = list(string.ascii_lowercase)
contraction = " ' ’ "
punctuation = "?!.,"
word_sol = {}
cipher = {}
word_bank = {}

def initialize_word_bank():
#creates a dictionary that organizes English words based on their length
# {2: "am", "is", etc.}
    for word in english_words:
        length = len(word)
        if length in word_bank:
            word_bank[length].append(word)
        else:
            word_bank[length] = [word]
    word_bank[1] = ["a", "i"]
    return word_bank

def initialize__sol(message):
#initializes word_sol and cipher dictionaries
    message = message.lower()
    m_words = message.split()
    m_spaceless = list(message.replace(" ", ""))
    m_letters = list(dict.fromkeys(m_spaceless))

    for l in m_letters:
        cipher[l] = alphabet
    for word in m_words:
        length = len(word)
        if length == 1:
            cipher[word] = ["a", "i"]
        word_sol[word] = word_bank[length]

    return cipher, word_sol

def duplicates():
#removes solutions from word_sol that don't fit duplicate pattern
    for word in word_sol:
        duplicates = []
        for letter in word:
            if word.count(letter) > 1 and letter not in duplicates:
                duplicates.append(letter)
        if len(duplicates) >= 1:
            code = codify(word)
            for sol in word_sol[word]:
                test_code = codify(sol)
                if test_code != code:
                    word_sol[word].remove(sol)

    return word_sol

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
    #i keeps track of what number each letter is
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
    for key, values in cipher.items():
        length = len(cipher[key])
        for value in values:
            input()
            print("the value we are on for the key: ", key, "is: ", value)
            print("Before", length)
            test_dict = word_sol.copy()
            test_letter = value
            encoded_letter = key
            print(cipher[encoded_letter])
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
                cipher[encoded_letter].remove(test_letter)
                print("after", length)







#set single letter to either "a" or "i"
#randomly assign cipher letters, if any of the words go empty, it can't english_words
#test this like 25*25 times for every alphabet letter.
#testing one at a time.

#letter dict: key is message letter, key value is alphabet letter
#assign the letter, and go through every encoded word that has that letter
#if word bank empty eliminate.

initialize_word_bank()
initialize__sol(message)
duplicates()
one_letter()

#pattern()
#one_letter()
