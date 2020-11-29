access = "y"
daftarNama = []
while access == "y" :
    data = str(input("Masukan nama Mahasiswa : "))
    daftarNama.append(data)
    access = str(input("Masukan lagi? (y/n)"))
    
daftarNama.sort()
daftar = tuple(daftarNama)
print()
print("Daftar Nama : ")
for i in range (len(daftarNama)) :
    print(daftarNama[i], " (", len(daftarNama[i]), " karakter )")
