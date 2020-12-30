#membuat kode program untuk membuat file berisi teks
#dan mengenkripsi file tersebut
file = open(r"d:\enkripsi.txt", "w+")

teks = str(input("""Masukan isi file (enkripsi.txt) yang akan dienkripsi,
(huruf Kapital) : """))
shift = int(input("Masukan angka pergeseran kode ASCII enkripsi: "))
""" menulis teks """
file.write(teks)
""" menampilkan is file yang telah dimasukan """
print("""       HASIL 
Isi File 1 (File Input) : """)
file.seek(0, 0)
isi = file.read()
print(isi)
print("""--------------------------------""")

string = ""
for char in isi :
    string = string + char
""" variabel 'string' berisi isi dari file """
""" isi file di enkripsi terlebih dahulu, disimpan ke dalam file baru
(enkripsi1.txt) """
#ENKRIPSI STRING, hasil = VAR enkripsi
enkripsi = ""
for char in string :
    if char == " " :
        karakter = " "
        enkripsi = enkripsi + karakter
    elif string.isupper() :
        charCode = ord(char)
        index = ord(char) - ord("A")
        newIndex = (index + shift) %26
        kode = newIndex + ord("A")
        karakter = chr(kode)
        enkripsi = enkripsi + karakter

""" membuat file dan memasukan isi file yg sudah di enkripsi
(var enkripsi) ke dalam file baru (enkripsi2.txt) """
#file enkripsi2.txt yg akan digunakan untuk input main program
berkas = open(r"d:\enkripsi2.txt", "w+")
berkas.write(enkripsi)
berkas.seek(0, 0)
print("""Isi File 2 (File ter-Enkripsi) : """)
print(berkas.read())
print("""--------------------------------""")
file.close()
berkas.close()

#MAIN PROGRAM (program yg diperintahkan di Praktikum 10 No.7)
""" mendekripsi isi file yang telah terenkripsi ke file baru """
file = open(r"d:\enkripsi2.txt", "r")
"""menyimpan isi file ke var teks """
teks = ""
for char in file :
    teks = teks + char
""" input pergeseran ASCII """
shift = int(input(""" *keterangan = angka pergeseran sebelumnya :"""+str(shift)+ """
Masukan angka pergeseran kode ASCII dekripsi :"""))


#DEKRIPSI, hasil VAR dekripsi
dekripsi = ""
for char in teks :
    if char == " " :
        karakter = " "
        dekripsi = dekripsi + karakter
    elif char.isupper() :
        charCode = ord(char)
        index = ord(char) - ord("A")
        newIndex = (index - shift) %26
        kode = newIndex + ord("A")
        karakter = chr(kode)
        dekripsi = dekripsi + karakter

""" membuat file enkripsi3.txt untuk output """
files = open(r"d:\enkripsi3.txt", "w+")
files.write(dekripsi)

#OUTPUT MAIN PROGRAM
files.seek(0, 0)
isiFile = files.read()
print("""     OUTPUT
Isi File 3 (File ter-Dekripsi) : """)
print(isiFile)
print("""--------------------------------""")
print("""
keterangan : 1. File 1 = d:\enkripsi.txt
             2. File 2 = d:\enkripsi2.txt
             3. File 3 = d:\enkripsi3.txt
             """)
#menutup file
file.close()
files.close()

