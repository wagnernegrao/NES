import os
from Crypto.Cipher import AES
from Crypto import Random


key = b'aula do samarone'  # 16 bits

#  message = str(input('Add text: '))
message = 'wagner'


def pad(message):
    '''
    Function pad:

    It receives the message and from its size adds bits to make it divisible
    by 16 so it is compatible with 3DES that checks for multiples of 16.

    From the generated value is concatenated the amount of '{' for the
    correct size.
    '''

    text = message + ((16 - len(message) % 16) * '{')

    return(text)


def encrypt(text, key):
    '''
    Function encrypt:

    Encrypt text
    '''
    iv = Random.new().read(AES.block_size)

    cipher = AES.new(key, AES.MODE_CBC, iv)  # Created object AES

    return(cipher.encrypt(text), cipher)


def decrypt(ciphertext, cipher):
    '''
    Function decrypt:

    Receive a ciphertext.
    Decrypt the text using utf-8 to remove 'b' verify of the encrypt.
    Remove '{' inserted in the process of pad.
    '''

    decodificed = cipher.decrypt(ciphertext).decode('utf-8')
    decodificed = decodificed.replace('{', '')

    return(decodificed)


text = pad(message)
# hash_key = generate_hash_key(key)
ciphertext, cipher = encrypt(text, key)
decrypted_text = decrypt(ciphertext, cipher)

print('\n')
print(f'Message: {message}')
# print(f'Hash key: {hash_key}')
print(f'Ciphertext: {ciphertext}')
print(f'Decrypted text: {decrypted_text}')
