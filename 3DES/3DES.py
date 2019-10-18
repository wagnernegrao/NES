import os
from Crypto.Cipher import DES3
from Crypto.Protocol.KDF import PBKDF2


key = 'aula do samarone'  # 16 bits

message = str(input('Add text: '))


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


def generate_hash_key(key, key_len=16):
    '''
    Function Generate hash key
    '''
    salt = os.urandom(8)

    hash_key = PBKDF2(key, salt, dkLen=key_len)

    return(hash_key)


def encrypt(text, key):
    '''
    Function encrypt:

    Encrypt text
    '''
    cipher = DES3.new(key, DES3.MODE_ECB)  # Create object 3DES

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
hash_key = generate_hash_key(key)
encrypted_text, cipher = encrypt(text, hash_key)
decrypted_text = decrypt(encrypted_text, cipher)

print('\n')
print(f'Message: {message}')
print(f'Hash key: {hash_key}')
print(f'Encrypted text: {encrypted_text}')
print(f'Decrypted text: {decrypted_text}')
