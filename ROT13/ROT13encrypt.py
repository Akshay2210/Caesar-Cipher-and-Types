
#ROT13 cipher is a special case of the Ceaser cipher in which the shift(key) is always 13.

a=str(input("Enter text to encrypt:"))
key=13
enc=""
for i in range (len(a)):
    char=a[i]
    if(char.isupper()):
        enc += chr((ord(char) + key-65) % 26 + 65)
    else:
        enc += chr((ord(char) + key-97) % 26 + 97)
print("Encrypted Text is:")
print(enc)
