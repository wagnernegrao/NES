from Crypto.Cipher import AES

key = b'aula do samarone'

message = str(input('Add text: '))
# message = '6 semestre'

cipher = AES.new(key)  # Obtemos um objeto para podermos criptografar


def pad(message):
    '''
    recebe o comprimento da mensagem e adiciona a quantidade de *
    para tornalauniformente divisilvel por 16, isso ocorre por causa do aes que
    tem dados de comprimento de 16 bits

    a partir do valor gerado concatena a quantidade de {
    '''
    text = message + ((16 - len(message) % 16) * '{') 

    return(text)


def encrypt(text):
    return(cipher.encrypt(text))


def decrypt(ciphertext):
    decodificed = cipher.decrypt(ciphertext).decode('utf-8') # para remover o b do inicio da string
    remove = str(dec).count('{')  # remove os { da palavra decifrada
    return(dec[:len(dec) - remove])  # apresenta ate aquele valor subtraido


pad_1 = pad(message)
enc = encrypt(pad_1)
dec = decrypt(enc)


print("Message:", message)

print("pad:", pad_1)

print("cifrado:", enc)

print("decifrado:", dec)
