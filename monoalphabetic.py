def mono(pt):
    pt = pt.replace(" ", "")
    al = "abcdefghijklmnopqrstuvwxyz"
    key = input("Enter key: ")
    en = ""
    de = ""

    for j in pt.lower():
        for i in al:
            if i == j:
                en+=key[al.index(i)]



    
    for j in en.lower():
        for i in key:
            if i == j:
                de+=al[key.index(i)]

    print("encrypted text: ", en)
    print("decrypted text", de)




pt = input("Enter plaintext: ")

mono(pt)
