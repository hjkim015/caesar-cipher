from PyDictionary import PyDictionary

#word_dict = PyDictionary()

sol_dict= dict{}
length_dict = {}

def length_dict():
    for key in word_dict:
        length = len(key)
        if length in length_dict:
            length_dict[length].append(key)
        else:
            length_dict[length] = key


    
