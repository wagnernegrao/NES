from Crypto.Cipher import DES3

key = 'aula do samarone'  # 16 bits
cipher = DES3.new(key, DES3.MODE_ECB)  # Create object 3DES

message = str(input('Add text: '))


def pad(message):

    text = message + ((16 - len(message) % 16) * '{')

    return(text)


def encrypt(text):
    '''
    Encrypt text
    '''

    return(cipher.encrypt(text))


def decrypt(ciphertext):
    decodificed = cipher.decrypt(ciphertext).decode('utf-8')
    decodificed = decodificed.replace('{', '')

    return(decodificed)



text = pad(message)
print(f"msg {len(message)}  - pad {len(text)}", )

test1 = encrypt(text)
print('-> ', test1)

test2 = decrypt(test1)
print('-> ', len(test2))
