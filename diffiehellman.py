#Diffie Hellman Key Exchange
from math import sqrt
# Returns True if n is prime 
def isPrime( n):
    # Corner cases
    if (n <= 1):
        return False
    if (n<= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i== 0 or n % (i + 2) == 0) :
            return False
        i= i + 6
    return True

def power(x,y,p):
    res = 1 # Initialize result 
    x = x % p # Update x if it is more
    # than or equal to p 
    while (y > 0):
    # If y is odd, multiply x with result 
        if (y & 1):
            res = (res * x) % p
            y = y>>1
            x = (x * x) % p
    return res
 
# Utility function to store prime # factors of a number 
def findPrimefactors(s, n) :
    while(n%2==0):
        # Print the number of 2s that divide n while (n % 2 == 0) :
        s.add(2)
        n = n // 2
        # n must be odd at this po. So we can # skip one element (Note i = i +2)
    for i in range(3, int(sqrt(n)), 2):
        # While i divides n, print i and divide n
        while (n % i == 0) :
            s.add(i)
            n = n // i
    if (n > 2) :
        s.add(n)
 
# Function to find smallest primitive # root of n 
def findPrimitive( n) :
    s= set()
    # Check if n is prime or not
    if (isPrime(n) == False):
        return -1
    # Find value of Euler Totient function
    # of n. Since n is a prime number, the # value of Euler Totient function is n-1 # as there are n-1 relatively prime numbers.
    phi = n - 1
    # Find prime factors of phi and store in a set
    findPrimefactors(s, phi)
    # Check for every number from 2 to phi
    for r in range(2, phi + 1):
        # Iterate through all prime factors of phi. # and check if we found a power with value 1
        flag = False
        for it in s:
            if (pow(r, phi // it,n) == 1):
                flag = True
                break
            # If there was no power with value 1.
        if (flag == False):
            return r
            # If no primitive root found
    return r
#generating public key of user A,B 
def pua(xa,a,q):
    if xa<q:
        ya=(a**xa)%q
        return ya
    else:
        print("xa should be < ", q)
        #key generation
def keyGen(x,y,q):
    k=(y**x)%q
    return k

q = int(input("Enter prime number:")) 
a=findPrimitive(q) 
xa=int(input("Enter private key of user A (<q) : ")) 
xb=int(input("Enter private key of user B (<q) : ")) 
ya=pua(xa,a,q) 
yb=pua(xb,a,q) 
ka=keyGen(xa,yb,q) 
kb=keyGen(xb,ya,q) 
print("Smallest primitive root of", q, "is", a)
print("ya=",ya)
print("yb=",yb)
print("ka=",ka)
print("kb=",kb)
