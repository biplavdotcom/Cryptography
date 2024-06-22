import random

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(a, p):
    m0, x0, x1 = p, 0, 1
    if p == 1:
        return 0
    while a > 1:
        q = a // p
        m0, a, p = a, p, a % p
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def elgamal_keygen(p):
    g = random.randint(2, p-1)
    x = random.randint(1, p-2)
    h = pow(g, x, p)
    return (p, g, h), x

def elgamal_encrypt(public_key, m):
    p, g, h = public_key
    y = random.randint(1, p-2)
    c1 = pow(g, y, p)
    s = pow(h, y, p)
    c2 = (m * s) % p
    return c1, c2

def elgamal_decrypt(private_key, p, c1, c2):
    x = private_key
    s = pow(c1, x, p)
    s_inv = modinv(s, p)
    m = (c2 * s_inv) % p
    return m
p = 467  
public_key, private_key = elgamal_keygen(p)
print(f"Public key: {public_key}")
print(f"Private key: {private_key}")

message = 123  # Example message (an integer)
print(f"Original message: {message}")

ciphertext = elgamal_encrypt(public_key, message)
print(f"Ciphertext: {ciphertext}")

decrypted_message = elgamal_decrypt(private_key, public_key[0], ciphertext[0], ciphertext[1])
print(f"Decrypted message: {decrypted_message}")