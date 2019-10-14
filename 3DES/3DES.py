import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


key = os.urandom(16)
beckend = default_backend()
text = "a secret message"

cipher = Cipher(algorithms.TripleDES(key), modes.ECB(), backend=beckend)

encryptor = cipher.encryptor()

ct = encryptor.update(b"{text}") + encryptor.finalize()

decryptor = cipher.decryptor()

print(f"Texto Encriptado: {ct}")

print(f"Text Decriptado{decryptor.update(ct) + decryptor.finalize()}")
