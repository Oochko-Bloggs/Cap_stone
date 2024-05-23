import hashlib
import sys


def detect_hash_type(hash_value):
    hash_length_to_type = {
        32: "MD5",
        40: "SHA1",
        56: "SHA224",
        64: "SHA256",
        96: "SHA384",
        128: "SHA512"
    }
    return hash_length_to_type.get(len(hash_value), None)


def get_hash(word, hash_type):
    if hash_type == "MD5":
        return hashlib.md5(word.encode('utf-8')).hexdigest()
    elif hash_type == "SHA1":
        return hashlib.sha1(word.encode('utf-8')).hexdigest()
    elif hash_type == "SHA224":
        return hashlib.sha224(word.encode('utf-8')).hexdigest()
    elif hash_type == "SHA256":
        return hashlib.sha256(word.encode('utf-8')).hexdigest()
    elif hash_type == "SHA384":
        return hashlib.sha384(word.encode('utf-8')).hexdigest()
    elif hash_type == "SHA512":
        return hashlib.sha512(word.encode('utf-8')).hexdigest()
    else:
        return None


hash_value = str(input("Enter the hash: "))

hash_type = detect_hash_type(hash_value)
if not hash_type:
    print("Unsupported or unknown hash type.")
    sys.exit()

print(f"Detected hash type: {hash_type}")

wordlist = '/home/splash/Downloads/20k.txt'

try:
    with open(wordlist, 'r') as file:
        words = file.read().splitlines()
except FileNotFoundError:
    print("The specified wordlist file was not found.")
    sys.exit()

found = False
for word in words:
    hashed_word = get_hash(word, hash_type)
    if hashed_word and hashed_word == hash_value:
        print(f"\033[1;32mHASH FOUND: {word}\033[0m")
        found = True
        break

if not found:
    print("\033[1;31mHASH NOT FOUND\033[0m")
