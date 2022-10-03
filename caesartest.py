import string
pt = str(input("Please enter your text : "))
k = int(input("Please enter the key : "))

pt = pt.lower()

alphabet = string.ascii_lowercase
shifted = alphabet[k:] + alphabet[:k]
table = str.maketrans(alphabet, shifted)

enc = pt.translate(table)
print("The encrypted text is : " ,enc)



