from Crypto.Cipher import DES3

key = 'aula do samarone'  # 16 bits
cipher = DES3.new(key, DES3.MODE_ECB)  # Create object 3DES

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


def encrypt(text):
    '''
    Function encrypt:

    Encrypt text
    '''

    return(cipher.encrypt(text))


def decrypt(ciphertext):
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
encrypted_text = encrypt(text)
decrypted_text = decrypt(encrypted_text)

print('\n')
print(f'Message: {message}')
print(f'Encrypted text: {encrypted_text}')
print(f'Decrypted text: {decrypted_text}')
