
alphabets=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
def getinput():
    k1=input("Type your message\n")
    k2=int(input("Type the shift number\n"))
    return (k1,k2)
def getindex(i):
    count=0
    for ig in alphabets:
        if(i==ig):
            break
        count+=1
    return count

def encrypt():
    encrypted_String=""
    g=getinput()
    for i in g[0]:
        if i in alphabets:
            k=(getindex(i)+g[1])%26
            encrypted_String+=alphabets[k]
        else:
            encrypted_String+=i
    print(f"Here's the Encrypted result: {encrypted_String}")
                    
def decrypt():
            decrypted_String=""
            g=getinput()
            for i in g[0]:
                if i in alphabets:
                    k=getindex(i)-g[1]
                    if(k>=0):
                        decrypted_String+=alphabets[k%26]
                    else:
                        decrypted_String+=alphabets[(k+26)%26]
                else:
                    decrypted_String+=i
            print(f"Here's the Decrypted result: {decrypted_String}")
def askagain():
    k1=input("type 'yes' to continue otherwise type no\n")
    if(k1=="yes"):
       k=ask()
    else:
        print("Good bye")
def ask():
    d=input("Type 'encrypt' for encryption 'decrypt' for decryption\n")
    if d=="encrypt":
        encrypt()
        askagain()
    elif d=="decrypt":
        decrypt()
        askagain()
ask()


