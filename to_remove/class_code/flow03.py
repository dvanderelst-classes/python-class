import string
message = 'take the castle at noon'
keyword = 'zebra'
alphabet = string.ascii_lowercase

# Make alphabet
cipher_alphabet = keyword
for x in alphabet:
    if x not in cipher_alphabet:
        cipher_alphabet = cipher_alphabet + x
    
cipher_alphabet = cipher_alphabet + ' '
alphabet = alphabet + ' '
    
# encode
encrypthed_message = ''
for letter in message:
    index = alphabet.find(letter)
    encrypthed_message = encrypthed_message + cipher_alphabet[index]
    
# decode
decrypthed_message = ''
for letter in encrypthed_message:
    index = cipher_alphabet.find(letter)
    decrypthed_message = decrypthed_message + alphabet[index]
    
print(encrypthed_message)
print(decrypthed_message)