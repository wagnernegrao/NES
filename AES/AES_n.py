from Crypto.Cipher import AES

key = b'aula do samarone'

message = str(input('Add text: '))
# message = '6 semestre'

cipher = AES.new(key)  # Obtemos um objeto para podermos criptografar


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
ciphertext = encrypt(text)
plaintext = decrypt(ciphertext)


print("Message:", message)

print("pad:", text, len(text))

print("cifrado:", ciphertext)

print("decifrado:", plaintext)
