alphabet = "abcdefghijklmnopqrstuvwxyz"

choice = int(raw_input("If you want to encode, type 1. If you want to decode, type 2: "))
code = raw_input("type the code here: ")
shift = int(raw_input("type the code shift # here: "))

def encoder_function(message_to_be_encoded, shift):
    encoder = ""

    for symbol in code:
        if symbol in alphabet:
            position = alphabet.find(symbol) + shift
            if position <= 25:
                new_symbol = alphabet[position]
            else:
            #makes up for the looping. If greater than alphabet index 25,
            #find the new index by subtracting 26
                position = position - 26
                new_symbol = alphabet[position]
            encoder = encoder + new_symbol
        else:
        #if it's not a letter it's a space that needs to be added
            encoder = encoder + " "

    raw_input("solved! Please press enter to view encoded message")
    print(encoder)
    return encoder

def decipher_function(message_to_be_deciphered,shift):
    #undoes the caesar cipher so goes backward with shift number
    decipher = ""
    for symbol in code:
        if symbol in alphabet:
            position = alphabet.find(symbol) - shift
            if position >= 0:
                new_symbol = alphabet[position]
            else:
                position = 26 + position
                new_symbol = alphabet[position]
            decipher = decipher + new_symbol

        else:
            decipher = decipher + " "
    raw_input("solved! Please press enter to view deciphered message")
    print(decipher)
    return decipher


def choose(choice):
    if choice == 1:
        encoder_function(code,shift)
    if choice == 2:
        decipher_function(code, shift)


choose(choice)


#action items:
    #sometimes the index can be out of range. Use mod
