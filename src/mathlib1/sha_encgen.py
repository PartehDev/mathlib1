import hashlib

def sha_enc(plain):
    enc1 = hashlib.sha384(plain)
    enc2 = hashlib.sha512(enc1)
    return enc2