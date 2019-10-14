import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()
key = os.urandom(32)
text = "a secret message"

cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)

encryptor = cipher.encryptor()

ct = encryptor.update(b"{text}") + encryptor.finalize()

decryptor = cipher.decryptor()

print(f"Texto Aberto: {text}")
print(f"Texto Encriptado: {ct}")
print(f"Texto Decriptado: {decryptor.update(ct) + decryptor.finalize()}")
