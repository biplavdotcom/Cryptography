import numpy as np

def gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = gcd(b % a, a)
        return g, y - (b // a) * x, x

def modinv(a, m):
    g, x, y = gcd(a, m)
    return x % m

def hill_encrypt(plain_text, key_matrix):
    key_matrix = np.array(key_matrix).reshape(2, 2)
    plain_text = plain_text.upper().replace(" ", "")
    while len(plain_text) % 2 != 0:
        plain_text += "Z"
    n = len(plain_text)
    result = ""
    for i in range(0, n, 2):
        pair = [ord(char) - 65 for char in plain_text[i:i+2]]
        encrypted_pair = np.dot(key_matrix, pair) % 26
        result += "".join([chr(num + 65) for num in encrypted_pair])
    return result

def hill_decrypt(encrypted_text, key_matrix):
    key_matrix = np.array(key_matrix).reshape(2, 2)
    key_matrix = np.array(key_matrix).reshape(2, 2)
    determinant = int(round(np.linalg.det(key_matrix))) % 26
    key_matrix_inv = np.array([[key_matrix[1][1], -key_matrix[0][1]], [-key_matrix[1][0], key_matrix[0][0]]])
    key_matrix_inv = (modinv(determinant, 26) * key_matrix_inv) % 26
    result = ""
    for i in range(0, len(encrypted_text), 2):
        pair = [ord(char) - 65 for char in encrypted_text[i:i+2]]
        decrypted_pair = np.dot(key_matrix_inv, pair) % 26
        result += "".join([chr(num + 65) for num in decrypted_pair])
    return result

key = [[5, 8], [17, 3]]
plain_text = "biplav ghale"
encrypted_text = hill_encrypt(plain_text, key)
decrypted_text = hill_decrypt(encrypted_text, key)
print("Plain Text:", plain_text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)