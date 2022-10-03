# def caesarcipher(pt, key):
#     pt = pt.replace(" ", "")
#     list1 = "abcdefghijklmnopqrstuvwxyz"
#     en = ""
#     for i in pt.lower():
#         k = (list1.index(i)+key)%26
#         en+=list1[k]
#     print("Encrypted text: ", en)
        
#     de=""
#     for j in en.lower():
#         k = (list1.index(j)-key)%26
#         de+=list1[k]
#     print("Decryted text: ", de)


# pt = input("Enter plain text: ")
# key = int(input("Enter key: "))


# caesarcipher(pt, key)










def caesarcipher(plaintext, key):
    al = "abcdefghijklmnopqrstuvwxyz"
    
    en = ""
    for i in plaintext.lower():
        formula = (al.index(i) + key) % 26
        en+=al[formula]
    print("Encrypted text: ", en)


    de = ""
    for i in en.lower():
        formula = (al.index(i) - key) % 26
        de += al[formula]
    print("Decrypted text: ", de)


plaintext = input("Enter plain text: ")
key = int(input("Enter key: "))

caesarcipher(plaintext, key)