from hashlib import sha256

input_ = input("Please input a phrase to encrypt.")
print(sha256(input_.encode("utf-8")).hexdigest())