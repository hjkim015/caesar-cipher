
from nltk.corpus import words
word_list = words.words()
#word_list = ["A", "a", "aa", "aal", "aalii", "aam", "Aani", "b", "sdfg"]
message = "ji he noem li gaiiag"

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


def length_sol_dict():
    for word in message:
        length = len(word)
        sol_dict[word] = length_dict[length]
        print(sol_dict)
        input()

create_length_dict()
length_sol_dict()
