from Crypto.Cipher import DES

key = 'hello123'

message = 'espero que funcione'

cipher = DES.new(key, DES.MODE_ECB)

def pad(message):

    text = message + ((8 - len(message) % 8) * ' ')

    return(text)


text = pad(message)
print(f"msg {len(message)}  - pad {len(text)}", )


def encrypt(text):
    return(cipher.encrypt(text))

test1 = encrypt(text)
print('-> ', test1)

def decrypt(ciphertext):
    return(cipher.decrypt(ciphertext).decode('uft-8'))

test2 = decrypt(test1)
print('-> ', test2)