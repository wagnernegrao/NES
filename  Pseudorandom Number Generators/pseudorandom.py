import os

# Generate a seed with os.urandom()
# This seed is converted to int with int.from_bytes()

for i in range(5, 13):
    print(f'{int.from_bytes(os.urandom(i), byteorder="big")}')
