from cryptography.fernet import Fernet
import os


def encrypt_file(file_name):
    # check if the user input file exist
    if os.path.exists(file_name):
        # Open the file to be encrypt
        if os.path.exists("key.txt"):
            # read the secret key from a file
            with open("key.txt", "r") as input_file:
                key = str.encode(input_file.read())
                eSecret = Fernet(key)
        else:
            # generate a key and write it to a file
            with open("key.txt", "w") as input_file:
                key = Fernet.generate_key()
                eSecret = Fernet(key)
                input_file.write(key.decode())
        # read the file and encrypt it's content
        with open(file_name, 'r') as input_file:
            plaintext = input_file.read()
            print("The selected file content is:", plaintext)
            byteValue = str.encode(plaintext)
            encryptedText = eSecret.encrypt(byteValue).decode()
            with open(file_name, 'w') as outputText:
                outputText.write(encryptedText)
        print("Done!")
    else:
        print("File not found")


def decrypt_file(file_name):
    # Open the input_file and decrypt the content
    if os.path.exists(file_name):
        with open("key.txt", "r") as input_file:
            kBytes = str.encode(input_file.read())
            dSecret = Fernet(kBytes)
        with open("test.txt", "r") as putText:
            text = str.encode(putText.read())
            print("The selected file content is:", text)
            decrypted = dSecret.decrypt(text).decode()
            with open("test.txt", "w") as input_file:
                input_file.write(decrypted)
        print("Done!")
    else:
        print("File not found")


while True:
    option = input("Enter E for encryption, D for decryption or X to quit: ")
    if option.upper() == "E":
        my_file = input("Enter the file name to start: ")
        encrypt_file(my_file)
    elif option.upper() == "D":
        my_file = input("Enter the file name to start: ")
        decrypt_file(my_file)
    else:
        break;