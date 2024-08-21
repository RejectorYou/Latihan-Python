import os,time,random

ulang=True

os.system('cls')

def piramida(p):
    os.system('cls')
    i=0
    j=int(p)
    pp=""

    if(j<3):
        j=3
    elif(j>60):
        j=60
    while(i<=j):
        k=j
        while(k>i):
            pp+=" "
            k-=1
        k=0
        while(k<i):
            pp+="*"
            k+=1
        k=1
        while(k<i):
            pp+="*"
            k+=1
        print(pp)
        pp=""
        i+=1
def menu1():
    os.system('cls')
    print(ll)
    p=input("Masukan Tinggi Piramida (min 3,max 60) : ")
    piramida(p)
    print(ll)
    print("Tinggi Piramida : ",p)
def menu2():
    os.system('cls')
    p=random.randrange(3,60)
    piramida(p)
    print(ll)
    print("Tinggi Piramida : ",p)
def loading():
    j=""
    i=0
    while(i<=100):
        k=random.randrange(1,100)
        print("Loading ",i,"%")
        print(j)
        j+="="
        i+=1
        k=k%3
        if(k<1):
            time.sleep(0.3)
        elif(k<2):
            time.sleep(0.05)
        else:
            time.sleep(0.1)
        os.system('cls')
    ll=j
    return ll

ll = loading()
#ll=""

while(ulang!=False):
    os.system('cls')
    print(ll)
    print("Piramida Bintang")
    print("1. Input Tinggi")
    print("2. Random")
    print(ll)
    menu=input("Pilih Menu : ")
    menu=int(menu)
    if(menu==1):
        menu1()
    elif(menu==2):
        menu2()
    else:
        print("gajelas")
    print(ll)
    pengulangan = input("Jalankan Lagi (y/t) : ")
    if(pengulangan=="y"):
        ulang=True
    else:
        ulang=False