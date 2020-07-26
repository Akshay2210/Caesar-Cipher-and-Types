decypt=""
c=str(input("Enter string to decrypt using bruteforce:"))
a=int(input("Enter starting key for bruteforce:"))
b=int(input("Enter ending key for bruteforce:"))
for i in range (a,(b+1)):
    for x in range (len(c)):
        char=c[x]
        if(char.isupper()):
            decypt += chr((ord(char) - i-65) % 26 + 65)
        else:
            decypt += chr((ord(char) -i-97) % 26 + 97)
    print("Decrypted text for key",i," is:")
    print(decypt)
    decypt=""
