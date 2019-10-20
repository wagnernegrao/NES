import os


for i in range(5, 13):
    print(f'{os.urandom(i)}')  # i is quantity of bits
