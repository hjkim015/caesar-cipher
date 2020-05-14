
from nltk.corpus import words
word_list = words.words()
#word_list = ["A", "a", "aa", "aal", "aalii", "aam", "Aani", "b", "sdfg"]

message = '''Ovg fh ivgfim uli z nlnvmg gl Ozwb Olevozxv’h lyqvxgrlm dsrxs hgzgvw gszg gsv nzxsrmv xzm lmob wl dszg dv gvoo rg gl wl'''
#message = "ji he noem li gaiiag"
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" + "’"
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

def initialize_sol():
    #sets each word in the message to a solution set equal to the word length
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

    for word in message_words:
    #matches each message word with potential solution list based on length
        length = len(word)
        sol_dict[word] = length_dict[length]





create_length_dict()
initialize_sol()
