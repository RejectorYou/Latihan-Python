import os

loop=True

def line():
    j=""
    i=0
    while(i<=100):
        j+="="
        i+=1

    return j

garis = line()


os.system('cls')

while loop == True:
    while True:
        try:
            print(garis)
            print("Aplikasi Menentukan Bilangan Ganjil atau Genap")
            print(garis)
            i=int(input("Masukan bilangan : "))
            break
        except:
            os.system('cls')
            print("Hanya masukan bilangan saja !!!")
    gg = i%2
    print(garis)
    if (gg==1):
        print("Variabel i=",i,"<- Adalah Bilangan Ganjil")
    else:
        print("Variabel i=",i,"<- Adalah Bilangan Genap")
    print(garis)
    loop = input("Try Agan ? (y/n)")
    loop = loop.upper()
    if loop=="Y":
        loop=True
        os.system('cls')
    else:
        break

