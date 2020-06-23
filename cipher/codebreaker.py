# credits for replace_string_function --> https://stackoverflow.com/questions/41752946/replacing-a-character-from-a-certain-index
# credits for find find_letter_indices function --> https://stackoverflow.com/questions/11122291/how-to-find-char-in-string-and-get-all-the-indexes
from nltk.corpus import words
import numpy as np
import string
import re

english_words = words.words()
message = '''Ovg fh ivgfim uli z nlnvmg gl Ozwb Olevozxv’h lyqvxgrlm, dsrxs hgzgvw gszg gsv nzxsrmv xzm lmob wl dszg dv gvoo rg gl wl. Lmv xlfow hzb gszg z nzm xzm "rmqvxg" zm rwvz rmgl gsv nzxsrmv, zmw gszg rg droo ivhklmw gl z xvigzrm vcgvmg zmw gsvm wilk rmgl jfrvhxvmxv, orpv z krzml hgirmt hgifxp yb z sznnvi. Zmlgsvi hrnrov dlfow yv zm zglnrx krov lu ovhh gszm xirgrxzo hrav: zm rmqvxgvw rwvz rh gl xliivhklmw gl z mvfgilm vmgvirmt gsv krov uiln drgslfg. Vzxs hfxs mvfgilm droo xzfhv z xvigzrm wrhgfiyzmxv dsrxs vevmgfzoob wrvh zdzb. Ru, sldvevi, gsv hrav lu gsv krov rh hfuurxrvmgob rmxivzhvw, gsv wrhgfiyzmxv xzfhvw yb hfxs zm rmxlnrmt mvfgilm droo evib orpvob tl lm zmw lm rmxivzhrmt fmgro gsv dslov krov rh wvhgilbvw. Rh gsviv z xliivhklmwrmt ksvmlnvmlm uli nrmwh, zmw rh gsviv lmv uli nzxsrmvh? Gsviv wlvh hvvn gl yv lmv uli gsv sfnzm nrmw. Gsv nzqlirgb lu gsvn hvvn gl yv "hfy xirgrxzo," r.v. gl xliivhklmw rm gsrh zmzoltb gl krovh lu hfy-xirgrxzo hrav. Zm rwvz kivhvmgvw gl hfxs z nrmw droo lm zeviztv trev irhv gl ovhh gszm lmv rwvz rm ivkob. Z hnzoorhs kilkligrlm ziv hfkvixirgrxzo. Zm rwvz kivhvmgvw gl hfxs z nrmw nzb trev irhv gl z dslov "gsvlib" xlmhrhgrmt lu hvxlmwzib, gvigrzib zmw nliv ivnlgv rwvzh. Zmrnzoh’ nrmwh hvvn gl yv evib wvurmrgvob hfy-xirgrxzo. Zwsvirmt gl gsrh zmzoltb dv zhp,"Xzm z nzxsrmv yv nzwv gl yv hfkvi-xirgrxzo?'''

#message = '''Ovg fh ivgfim uli z nlnvmg gl Ozwb Olevozxv’h lyqvxgrlm, dsrxs hgzgvw gszg gsv nzxsrmv xzm lmob wl dszg dv gvoo rg gl wl.'''

alphabet = list(string.ascii_lowercase)
contraction = " ' ’ "
punctuation = "?!.,"
word_sol = {}
cipher = {}
word_bank = {}

def initialize_word_bank():
    '''creates a dictionary that organizes English words based on their length.
    All letters will be lowercase'''

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
    message = ' '.join(word.strip(string.punctuation) for word in message.split())
    #strips punctuation
    m_words = message.split()

    m_spaceless = list(message.replace(" ", ""))
    m_letters = list(dict.fromkeys(m_spaceless))

    for l in m_letters:
        cipher[l] = alphabet[:]
    for word in m_words:
        length = len(word)
        if length == 1:
            cipher[word] = ["a", "i"]
        word_sol[word] = word_bank[length].copy()

    return cipher, word_sol

def duplicates():
    '''returns a modified word_sol dictionary that has removed solutions that
    don't fit the duplicates pattern. For example, the word aal will be removed
    from the the potential solutions for the encoded word ovg because ovg
    does not have any duplicate letters like aal'''

    for word in word_sol:
        # input("_____________________________________________________")
        duplicates = []
        for letter in word:
            code = codify(word)
            for sol in word_sol[word]:
                before = len(word_sol[word])
                test_code = codify(sol)
                # print(word, sol)
                # print(code, test_code)
                if test_code != code:
                    word_sol[word].remove(sol)
                    after = len(word_sol[word])
                    # print(word, sol)
                    # print("removed!", before, "-->", after)
                    # print("ivgfim", len(word_sol["ivgfim"]))

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
    '''returns a list of the index positions of a specific letter in a word'''
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



def one_letter_cipher_test(encoded_letter, test_letter):
    '''takes a potential one_letter cipher mapping and returns a 1 or 0 whether the cipher
    could be a solution for the message'''

    test_dict = word_sol.copy()
    results = []
    for encoded_word in test_dict:
        if encoded_letter in encoded_word:
            result = cipher_word(encoded_letter, encoded_word, test_letter, test_dict)
            results.append(result)

    if 0 in results:
        # print("not a potential cipher. please remove")
        verdict = 0
        return verdict
    else:
        verdict = 1
        # print("a potential solution")
        return verdict

def cipher_word(encoded_letter, encoded_word, test_letter, test_dict):
    '''This function is used for the _cipher_test function. It returns a 1 or 0 to show
    whether a test_letter can be a solution for one encoded word'''
    indices = find_letter_indices(encoded_word, encoded_letter)
    # print("length --> of solutions for this word", len(test_dict[encoded_word]))
    for sol in test_dict[encoded_word]:
        if sol[indices[0]] == test_letter:
            # print("sol", sol)
            result = 1
            return result

    result = 0
    return result


def cipher_test():
    '''will run through the whole entire cipher and will eliminate test_letters
    that cannot be potential solutions for the message.'''

    for encoded_letter, values in cipher.items():
        print(encoded_letter, "values before", len(cipher[encoded_letter]))

        for test_letter in values[::-1]:
            # print("test_letter", test_letter)
            result = one_letter_cipher_test(encoded_letter, test_letter)
            if result == 0:
                cipher[encoded_letter].remove(test_letter)
        print(encoded_letter, "after-->", len(cipher[encoded_letter]))
        input("_________________________________________________")

    return cipher



'''action items:
    1.) convert the english words to lowercase so they're easier to work with.

'''


initialize_word_bank()
initialize__sol(message)
duplicates()
cipher_test()

#cipher_test()
