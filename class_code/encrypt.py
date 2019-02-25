import string

def unique(keyword):
    keyword = keyword.lower()
    keyword = ''.join(sorted(set(keyword), key=keyword.index))
    return keyword

def make_alphabets(keyword):
    keyword = unique(keyword)
    alphabet = string.ascii_lowercase
    cipher_alphabet = keyword
    for x in alphabet:
        if x not in cipher_alphabet:
            cipher_alphabet = cipher_alphabet + x
    cipher_alphabet = cipher_alphabet + ' '
    alphabet = alphabet + ' '
    return alphabet, cipher_alphabet

def encrypt(message, keyword):
    message = message.lower()
    alphabet, cipher_alphabet = make_alphabets(keyword)
    encrypthed_message = ''
    for letter in message:
        index = alphabet.find(letter)
        encrypthed_message = encrypthed_message + cipher_alphabet[index]
    return encrypthed_message

def decrypt(encrypthed_message, keyword):
    encrypthed_message = encrypthed_message.lower()
    alphabet, cipher_alphabet = make_alphabets(keyword)
    decrypthed_message = ''
    for letter in encrypthed_message:
        index = cipher_alphabet.find(letter)
        decrypthed_message = decrypthed_message + alphabet[index]
    return decrypthed_message
            
    