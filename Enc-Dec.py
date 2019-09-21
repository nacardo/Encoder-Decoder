import string
alphabet = string.ascii_lowercase
alpha2 = alphabet * 2 # create a loop of the alphabet

def msg_encoder(msg, en_key):
    new_msg = ''
    for letter in msg: # iterate over each letter in the user's message
        if  letter in alphabet: # if the letter is in our alphabet
            new_msg += alpha2[alphabet.index(letter) + en_key] # change the letter to represent the new key
        else:
            new_msg += letter
    return new_msg

def msg_decoder(msg, en_key):
    new_old_msg = ''
    for letter in msg: # iterate over each letter in the user's message
        if  letter in alphabet: # if the letter is in our alphabet
            new_old_msg += alpha2[alphabet.index(letter) - en_key] # change the letter to represent the new key
        else:
            new_old_msg += letter
    return new_old_msg

def encode():
    message = input("Type your message: ").lower() #obtain users message
    enc_key = int(input("Which key would you like to use? (1-25) ")) #ask user which key they want to use
    return (msg_encoder(message,enc_key))

def decode():
    enc_msg = input('Type your encoded message here: ')
    enc_key = int(input('Enter the key: '))
    return msg_decoder(enc_msg, enc_key)
