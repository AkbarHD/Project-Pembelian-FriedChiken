from time import perf_counter


print("****************Toko Mas Asu**************************")
print("kode        Menu                           Harga")
print("MA          Mie Ayam                       Rp. 10.000")
print("MAB         Mie Ayam Bakso                 Rp. 15.000")
print("BU          Bakso Urat                     Rp. 13.000")
print("BT          Bakso Telur                    Rp. 12.000")
print("*******************************************************")

banyak_jenis = int(input("Banyak jenis : "))
kode = []
menu = []
harga = []
banyak_potong = []
jumlah = []

i = 0
while i < banyak_jenis:
    print("jenis ke",i+1)
    kode.append(input("MASUKAN kode : [MA/MAB/BU/BT]"))
    banyak_potong.append(int(input("Total beli : ")))

    if kode[i]=="MA" or kode[i]=="MA":
        menu.append("Mie Aayam")
        harga.append("10000")
        jumlah.append(banyak_potong[i]*int("10000"))
    elif kode[i]=="MAB" or kode[i]=="MAB":
        menu.append("Mie Ayam Bakso")
        harga.append("15000")
        jumlah.append(banyak_potong[i]*int("15000"))
    elif kode[i]=="BU" or kode[i]=="BU":
        menu.append("Bakso Urat")
        harga.append("13000")
        jumlah.append(banyak_potong[i]*int("130000"))
    elif kode[i]=="BT" or kode[i]=="BT":
        menu.append("Bakso telur")
        harga.append("120000")
        jumlah.append(banyak_potong[i]*int("120000"))
    else:
        menu.append("kode salah")
        harga.append("0")
        jumlah.append(banyak_potong[i]*int("0"))
    i=i+1

jumlah_bayar = 0
a = 0
while a < banyak_jenis:
    jumlah_bayar = jumlah_bayar+jumlah[a]
    print("%i    %s     %s        %s         %i"%(a+i,menu[a],harga[a],banyak_potong[a],jumlah[a]))
    a=a+1

print("**********************Transaksi Pembayaran******************")
print("anda harus membayar : ",jumlah_bayar)
ubay = int(input("uang bayar anda : "))
kembalian = ubay - jumlah_bayar
print("ini uang kembalian anda : ",kembalian)
print("***************************************************")
print("==============Anda mendapatkan Bonus===================")
bonus = ["Boneka","TAS"]
for x in range(len(bonus)):
    print("1.",bonus[x])
print("=============Terimas kasih dan selamat berbelanja==============")
    
    







        

        

