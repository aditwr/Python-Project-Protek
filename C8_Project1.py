a = int(input("Masukan jumlah perulangan : "))
daftarBil = []
for i in range (a) : 
    bil = int(input("Masukan Bilangan : "))
    daftarBil.append(bil)
daftarBil.sort(reverse=True)
print("Daftar bilangan terurut dari besar ke kecil : ")
print(daftarBil)
