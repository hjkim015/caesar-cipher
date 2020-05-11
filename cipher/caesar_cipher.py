


alphabet = "abcdefgijklmnopqrstuvwxyz"

code = raw_input("type the code to be deciphered here: ")
shift = int(raw_input("type the code shift # here: "))

def decipher_function(code, shift):
    decipher = ""

    for symbol in code:
        if symbol in alphabet:
            position = alphabet.find(symbol) + shift
            new_symbol = alphabet[position]
            decipher = decipher + new_symbol
        else:
        #if it's not a letter it's a space that needs to be added
            decipher = decipher + " "

    raw_input("solved! Please press enter to view decipher")
    print(decipher)
    return decipher

decipher_function(code, shift)


#action items:
    #sometimes the index can be out of range. Use mod
