import os,time,os

a=0
b=""
c=0
loop=True


os.system('cls')

a=input("NOMBER : ")
a=int(a)
while (loop==True):
    b=input("SIMBOL : ")
    b=str(b)
    if(b=="="):
        break
    c=input("NOMBER : ")
    c=int(c)
    if(b=="+"):
        a+=c
    elif(b=="-"):
        a-=c
    elif(b=="*"):
        a*=c
    elif(b=="/"):
        a/=c
print(int(a))