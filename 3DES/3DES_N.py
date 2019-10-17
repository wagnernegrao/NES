from Crypto.Cipher import DES3

key = 'aula do samarone'  # 16 bits

message = str(input('Add text: '))
#message = 'espero que funcione'

cipher = DES3.new(key, DES3.MODE_ECB)

def pad(message):

    text = message + ((16 - len(message) % 16) * '{')

    return(text)


text = pad(message)
print(f"msg {len(message)}  - pad {len(text)}", )


def encrypt(text):
    return(cipher.encrypt(text))

test1 = encrypt(text)
print('-> ', test1)

def decrypt(ciphertext):
    decodificed = cipher.decrypt(ciphertext).decode('utf-8')
    decodificed = decodificed.replace('{', '')

    return(decodificed)


test2 = decrypt(test1)
print('-> ', len(test2))