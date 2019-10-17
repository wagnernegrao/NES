from Crypto.Cipher import AES

key = b'aula do samarone'

# message = str(input())
message = '6 semestre'


cipher = AES.new(key)  # Obtemos um objeto para podermos criptografar


def pad(s):
    '''
    recebe o comprimento da mensagem e adiciona a quantidade de *
    para tornalauniformente divisilvel por 16, isso ocorre por causa do aes que
    tem dados de comprimento de 16 bits
    '''
    value = s + ((16 - len(s) % 16) * '{')

    return(value)


def encrypt(text):
    return(cipher.encrypt(text))
