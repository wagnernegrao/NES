from Crypto.Cipher import DES

key = 'aula do samarone'

message = 'espero que funcione'

cipher = DES.new(key, DES.MODE_ECB)

def pad(message):

    text = message + ((8 - len(message) % 8) * ' ')

    return(text)

text = pad(message)
print(f"msg {len(message)}  - pad {len(text)}", )

def encrypt(text):
    return(cipher.encrypt(text))

