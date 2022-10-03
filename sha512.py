import hashlib
def sha(m):
    m=m.encode("utf8")
    hash512=hashlib.sha1(m)
    print("SHA-512 signature of Your Message is:",hash512.hexdigest())
pt=input("Enter a Message:")
sha(pt)
