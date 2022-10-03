import hashlib
def sha(m):
    m=m.encode("utf8")
    hash1=hashlib.sha1(m)
    print("SHA-1 signature of Your Message is:",hash1.hexdigest())
pt=input("Enter a Message:")
sha(pt)
