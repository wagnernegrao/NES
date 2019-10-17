from Crypto.Cipher import DES

key = 'aula do samarone'

message = 'espero que funcione'


def pad(message):

    text = message + ((8 - len(message) % 8) * ' ')

    return(text)
