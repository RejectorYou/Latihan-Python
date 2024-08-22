import os,time,random,datetime

barang_nama=["","RAM","Prosesor","VGA","SSD","HDD","Mouse","Keyboard","Flashdisk"]
barang_harga=[0,300000,1500000,3200000,1000000,800000,50000,200000,100000]
beli_nama=[]
beli_harga=[]
beli_code=""
total_harga=0
garis = ""
lb=0

def loading():
    j=""
    i=0
    while(i<=100):
        k=random.randrange(1,100)
        print(j)
        print("Kasir 1.2")
        print(j)
        print("Loading ",i,"%")
        print(j)
        j+="="
        i+=1
        k=k%3
        if(k<1):
            time.sleep(0.03)
        elif(k<2):
            time.sleep(0.005)
        else:
            time.sleep(0.01)
        os.system('cls')
    return j

def closing():
    j=""
    while len(j)<=100:
        j+="="
    i=100
    while(i>=0):
        k=random.randrange(1,100)
        print(j)
        print("Terimakasih")
        print(j)
        print("Closing ",i,"%")
        print(j)
        j=j[:-1]
        i-=1
        k=k%3
        if(k<1):
            time.sleep(0.01)
        elif(k<2):
            time.sleep(0.001)
        else:
            time.sleep(0.01)
        os.system('cls')
    return j

menu=True
garis = loading()
while menu == True:
    loop=True
    while loop == True:
        os.system('cls')
        while True:
            try:
                print(garis)
                for i in range(len(barang_harga)):
                    if i != 0:
                        print(i,". ",barang_nama[i],"\t\t\t Rp. ",barang_harga[i])
                print(garis)
                if total_harga:
                    print(beli_code[:-1])
                    print(garis)
                lb =  int(input("Masukan Kode barang (input 0 jika selesai belanja) : "))
                break
            except:
                os.system('cls')
                print(garis)
                print("Hanya input nomber saja !")
                print(garis)
                time.sleep(1)
                os.system('cls')
        if lb>=1 and lb<=8:
            beli_nama.append(barang_nama[lb])
            beli_harga.append(barang_harga[lb])
            beli_code = beli_code+str(lb)+","
            total_harga+=barang_harga[lb]
        elif lb >8:
            os.system('cls')
            print(garis)
            print("Barang Belum Tersedia")
            print(garis)
            time.sleep(1)
            os.system('cls')
        elif lb == 0:
            break
        else:
            break
    os.system('cls')
    print(garis)
    print(datetime.datetime.now(),"\tStruk Pembelian")
    print(garis)
    for i in range(len(beli_harga)):
        print(i+1,".\t",beli_nama[i],"\t\t\tRp. ",beli_harga[i])
    print(garis)
    print("Total Harga : Rp. ",total_harga)
    print(garis)
    
    menu = input("Back To Menu (T/U/S) : ")
    menu=menu.upper()
    if menu==False:
        closing()
        break
    else:
        if menu=="T":
            os.system('cls')
        elif menu=="U":
            os.system('cls')
            beli_code=""
            beli_harga=[]
            beli_nama=[]
            total_harga=0
        else:
            closing()
            break
        menu=True