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
    decodificed = cipher.decrypt(ciphertext).decode('utf-8') # para remover o b do inicio da string
    remove = str(decodificed).count('{')  # remove os { da palavra decifrada
    return(decodificed[:len(decodificed) - remove])  # apresenta ate aquele valor subtraido


text = pad(message)
ciphertext = encrypt(text)
plaintext = decrypt(ciphertext)


print("Message:", message)

print("pad:", text, len(text))

print("cifrado:", ciphertext)

print("decifrado:", plaintext)
