

a=str(input("Enter text to encrypt:"))
key=13
decypt=""
for i in range (len(a)):
    char=a[i]
    if(char.isupper()):
        decypt += chr((ord(char) - key-65) % 26 + 65)
    else:
        decypt += chr((ord(char) - key-97) % 26 + 97)
print("Dencrypted Text is:")
print(decypt)
