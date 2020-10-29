#Program menghitung gaji karyawan bersadarkan aturan Perusahaan

print("=" * 50)
print("Selamat Datang di Aplikasi Gaji Perusahaan")
print("_" * 50)
#input data
print("Masukan Kode Karyawan")
code = input()
print("Masukan Nama Anda")
name = input()
print("Masukan Golongan Karyawan")
print(" Golongan Karyawan : A, B, C, D")
gol = input()

while not (gol == "A" or gol == "B" or gol == "C" or gol == "D") :
    print("Masukan ulang Golongan Karyawan, input A, B, C, D")
    gol = input()
    if (gol == "A" or gol == "B" or gol == "C" or gol == "D") :
        break

#Menghitung Variabel
if gol == "A":
    gajiPokok = 10000000
    p = 2.5
    potongan = (p/100) * gajiPokok
    gajiBersih = gajiPokok - potongan
elif gol == "B" :
    gajiPokok = 8500000
    p = 2
    potongan = (p/100) * gajiPokok
    gajiBersih = gajiPokok - potongan
elif gol == "C":
    gajiPokok = 7000000
    p = 1.5
    potongan = (p/100) * gajiPokok
    gajiBersih = gajiPokok - potongan
elif gol == "D":
    gajiPokok = 5500000
    p = 1
    potongan = (p/100) * gajiPokok
    gajiBersih = gajiPokok - potongan
    

#Menampilkan output
    
print("=" * 50)
print("STRUCK RINCIAN GAJI KARYAWAN")
print("_" * 50)

print(" Nama Karyawan : ", name,)
print(" Golongan : ", gol,)
print("-" * 50)
print(" Gaji Pokok : Rp", gajiPokok,)
print(" Potongan " "(", p , "%)" " = Rp", potongan,)
print("-" * 50)
print(" Gaji Bersih : Rp", gajiBersih,)
