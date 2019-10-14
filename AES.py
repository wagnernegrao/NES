from Crypto.Cipher import AES

key = "Sixteen byte key"

plain = "Secret: 16 bytes"

cipher = AES.new(key)

ciphertext = cipher.encrypt(plain)

print(f"{ciphertext.encode("hex")}")

print(f"Decrypt: {cipher.decrypt(ciphertext)}")