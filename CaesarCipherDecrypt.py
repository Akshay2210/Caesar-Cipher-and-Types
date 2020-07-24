
a=str(input("Enter encrypted text:"))
key=int(input("Enter key:"))
decypt=""
for i in range (len(a)):
    char=a[i]
    if(char.isupper()):
        decypt += chr((ord(char) - key-65) % 26 + 65)
    else:
        decypt += chr((ord(char) - key-97) % 26 + 97)
print("Decrypted text is:")
print(decypt)
