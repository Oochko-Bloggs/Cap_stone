from cryptography.fernet import Fernet
import getpass


def encrypt_file(filename, key, password):
    try:
        with open(filename, 'rb') as file:
            original_data = file.read()

        f = Fernet(key)
        encrypted_data = f.encrypt(original_data)

        with open(filename + '.enc', 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

        with open(filename + '.pwd', 'wb') as pwd_file:
            pwd_file.write(password.encode())

        print("Encryption successful")
    except Exception as e:
        print(f"An error occurred during encryption: {e}")


def decrypt_file(filename, key, password):
    try:
        with open(filename + '.enc', 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()

        f = Fernet(key)
        decrypted_data = f.decrypt(encrypted_data)

        return decrypted_data.decode()
    except Exception as e:
        print(f"An error occurred during decryption: {e}")


def main():

    file_path = input("[*] Enter Path Of the text file: ")
    password = getpass.getpass("Enter the password: ")

    # Load encryption key
    with open('mykey.key', 'rb') as mykey:
        key = mykey.read()

    # Encrypt file
    encrypt_file(file_path, key, password)

    # Decrypt file and print content
    decrypted_content = decrypt_file(file_path, key, password)
    print("Decrypted content:")
    print(decrypted_content)


if __name__ == "__main__":
    main()
