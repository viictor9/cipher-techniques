def gcd(m,n):
    if m<n:
        (m,n)=(n,m)
    if(m%n)==0:
        return n
    else:
        return(gcd(n,m%n))#Recursion taking place
def rsaAlgo(p,q):
    print("p=",p,"q=",q)
    n=p*q
    fin=(p-1)*(q-1)
    for i in range(1,fin):
        if gcd(i,fin)==1:
            e=i
            d=i
    print("d=",d)
    #Encryption
    print("Enter Message such that Message<",n)
    message=int(input(""))
    enc=message**e%n
    print("enc=",enc)

    #Decryption
    print("Enter c such that c<",n)
    cipher=int(input(""))
    dec=cipher**d%n
    print("dec=",dec)
def primeNum(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                print("Invalid")
                n=int(input("Enter a Prime Number"))
        else:
            print("Valid")
    else:
        print()
    return n
p=int(input("Enter A Prime Number:"))
p1=primeNum(p)
q=int(input("Enter Another Prime Number:"))
q1=primeNum(q)
rsaAlgo(p1,q1)
