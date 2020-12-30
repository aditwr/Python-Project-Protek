import random
print("""Program membuat file.txt""")
n = int(input("Masukan Jumlah bilangan acak yg akan dimasukan ke dalam file.txt : "))
a = int(input("Berapa angka batas terkecil bilangan acak? : "))
z = int(input("Berapa angka batas terbesarnya? : "))
file = open(r"d:\bil.txt", "w+")
listBil = []
sum = 0
for i in range(n) :
    bil = random.randint(a, z)
    listBil.append(bil)
    file.write(str(bil)+"\n")
    sum = sum + bil
file.seek(0, 0)
isi = file.read()
genap = 0
ganjil = 0
for i in listBil :
    if i%2 == 0 :
        genap = genap + 1
    elif i%2 == 1 :
        ganjil = ganjil + 1
average = sum/n

print("""

===========================
Daftar Angka :
---------------------------""")
print(isi)
print("""---------------------------""")
print("""Statistik :
    Jumlah(n) bilangan : """, n, """
    Jumlah bil genap   : """, genap, """
    Jumlah bil ganjil  : """, ganjil,"""
    Nilai Max          : """, max(listBil),"""
    Nilai Min          : """, min(listBil), """
    Rata-rata          : """, round(average, 2),"""
===========================""")


