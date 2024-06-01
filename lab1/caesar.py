def encypt_func(txt, s):
    result = ""
# transverse the plain txt
    for i in range(len(txt)):
        char = txt[i]
        # encypt_func uppercase characters in plain txt

        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        # encypt_func lowercase characters in plain txt
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result
# check the above function
txt = "biplav ghale"
s = 2
result=encypt_func(txt, s)

print("Plain txt : " + txt)
print("Shift pattern : " + str(s))
print("Cipher: " + result)

def decrypt(cipher_txt,s):
    decrypt_text= ""
    for i in range(len(cipher_txt)):
        char = cipher_txt[i]
        if (char.isupper()):
            decrypt_text += chr((ord(char) - s - 65) % 26 + 65)
        else:
            decrypt_text += chr((ord(char) - s - 97) % 26 + 97)
    return decrypt_text

print("Decrypted text: " + decrypt(result, s))
