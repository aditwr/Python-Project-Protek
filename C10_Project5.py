file = open(r"d:\bilangan.txt", "r")
berkas = open("d:\hasilBil.txt", "w+")
print("""   Menampilkan isi file input (bilangan.txt) : """)
for line in file :
    bil1, bil2 = line.split("|")
    bil1 = int(bil1)
    bil2 = int(bil2)
    print(bil1, end=' | ')
    print(bil2)
    hasil = bil1 + bil2
    hasil = str(hasil)
    

    berkas.write(hasil + "\n")

file.close()
berkas.close()

file = open(r"d:\hasilBil.txt", "r")
print("""
    Isi file hasil penjumlahan (hasilBil.txt) : """)
print(file.read())
