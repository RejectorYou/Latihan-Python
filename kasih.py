import os,time,random,datetime
barang_nama=["","RAM","Prosesor","VGA","SSD","HDD","Mouse","Keyboard","Flashdisk"]
barang_harga=[0,300000,1500000,3200000,1000000,800000,50000,200000,100000]
beli_nama=[]
beli_harga=[]
beli_code=""
total_harga=0






menu=True
while menu == True:
    loop=True
    while loop == True:
        os.system('cls')
        print("===============================================================")
        for i in range(len(barang_harga)):
            if i != 0:
                print(i,". ",barang_nama[i],"\t\t\t Rp. ",barang_harga[i])
                
        print("===============================================================")
        if total_harga:
            print(beli_code[:-1])
            print("===============================================================")
        lb=input("Masukan Kode barang (input kosong jika selesai belanja) : ")
        if lb:
            lb=int(lb)
            beli_nama.append(barang_nama[lb])
            beli_harga.append(barang_harga[lb])
            beli_code = beli_code+str(lb)+","
            total_harga+=barang_harga[lb]
        else:
            break
    os.system('cls')
    print("===============================================================")
    print(datetime.datetime.now(),"\tStruk Pembelian")
    print("===============================================================")
    for i in range(len(beli_harga)):
        print(i+1,".\t",beli_nama[i],"\t\t\tRp. ",beli_harga[i])
    print("===============================================================")
    print("Total Harga : Rp. ",total_harga)
    print("===============================================================")
    menu = input("Back To Menu (T/U/S) : ")
    menu=menu.upper()
    if menu==False:
        os.system('cls')
        print("===============================================================")
        print("GOOD BYE")
        print("===============================================================")
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
            os.system('cls')
            print("===============================================================")
            print("GOOD BYE")
            print("===============================================================")
            break
        menu=True