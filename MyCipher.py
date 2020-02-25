# ICS483 Group Project
# Authors: Kekeli D Akouete, Vang Uni A
# Implementing encryption in an application

from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class MyCipher:
    def __init__(self):
        self.initialvalue = b''

    def encryptAES_128(self, plaintext, key):
        cipher = AES.new(key, AES.MODE_CBC)
        plaintext = str.encode(plaintext)
        encrypted = cipher.encrypt(pad(plaintext, AES.block_size))
        self.initialvalue = b64encode(cipher.iv).decode('utf-8')
        ciphertext = b64encode(encrypted).decode('utf-8')
        result = (self.initialvalue, ciphertext)
        return result

    def decryptAES_128(self, key, iv, ciphertext):
        try:
            self.initialvalue = b64decode(iv)
            ciphertext = b64decode(ciphertext)
            cipher = AES.new(key, AES.MODE_CBC, self.initialvalue)
            plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size).decode()
            return plaintext
        except ValueError as error:
            error = "Wrong key or IV provided"
            return error

    def keygen(self):
        # Generate a random 16-bytes (128-bits)key and return it to the caller
        key = get_random_bytes(16)
        # print(key.hex().upper())
        return key


# c = MyCipher()
# myKey = c.keygen()
# print(myKey.hex().upper())
# with open("test.txt", 'r') as fd:
#     content = fd.read()
#     encrypt = c.encryptAES_128(content, myKey)
# ptext = c.decryptAES_128(myKey, encrypt[0], encrypt[1])
# print(ptext)
