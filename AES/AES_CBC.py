import os
from Crypto.Cipher import AES


key = 'aula do samarone'  # 16 bits

#  message = str(input('Add text: '))
message = 'wagner'


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