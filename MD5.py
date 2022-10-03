import hashlib
def file_check(filename):
    hash1=hashlib.md5()
    with open(filename,'rb')as open_file:
        content=open_file.read()
        hash1.update(content)
    print(hash1.hexdigest())
def pass_check(pw):
    hash1=hashlib.md5(pw.encode('utf-8'))
    print("Your md5 password is",hash1.hexdigest())
print("_MD5_")
print("1.File_Check \n 2.Password_Check")
choice=int(input("Please Enter Your Choice:"))
if(choice==1):
    print("File Check")
    fn='hello.txt'
    file_check(fn)
elif(choice==2):
    print("Password Check")
    pw=input("Enter A Password")
    pass_check(pw)
else:
    print("Wrong Choice") 
