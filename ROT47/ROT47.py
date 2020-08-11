#ROT47
a=str(input("Enter text:"))
enc=""
for i in range (len(a)):
    char=ord(a[i])
    if(char in range(33,127)):
        enc+=chr(33+((char+14) % 94))

x=str(input("Enter E to encrypt the text and D to decrypt the text:"))
if (x=="E"):
    print("Encrypted Text is:")
elif(x=="D"):
    print("Decrypted Text is:")

print(enc)
