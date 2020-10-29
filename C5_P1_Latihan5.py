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
#tambah variabel tunjangan nikah dan tunjangan anak
print("Masukan Status Pernikahan (1=Menikah & 0=Lajang)", end=' ')
status = int(input())

while status == 1 or status == 0 :
    if status == 1 :
        print("Memproses")
        print("Masukan Jumlah Anak", end=' = ')
        jmlAnak = int(input())
        break
    else :
        print("input harus berupa Angka 1 atau 2")
        print("Masukan Ulang Jumlah Anak, Jika tidak ada isi nol")
        jmlAnak = int(input())
        continue

tN = 10
tunjanganNikah = (tN/100)

tA = 5
tunjanganAnak = (jmlAnak*(tA/100))

#syarat
if status == 1 :
    tunjanganNikah = tunjanganNikah
    if jmlAnak !=0 :
        tunjanganAnak = tunjanganAnak
    elif jmlAnak == 0 :
        tunjanganAnak = 0
elif status == 0 :
    tunjanganNikah = 0
    tunjanganAnak = 0

#Menghitung Variabel
if gol == "A":
    gajiPokok = 10000000
    gajiKotor = gajiPokok + (tunjanganNikah*gajiPokok) + (tunjanganAnak*gajiPokok)
    p = 2.5
    potongan = (p/100) * gajiPokok
    gajiBersih = gajiKotor - potongan
elif gol == "B" :
    gajiPokok = 8500000
    gajiKotor = gajiPokok + (tunjanganNikah*gajiPokok) + (tunjanganAnak*gajiPokok)
    p = 2
    potongan = (p/100) * gajiPokok
    gajiBersih = gajiKotor - potongan
elif gol == "C":
    gajiPokok = 7000000
    gajiKotor = gajiPokok + (tunjanganNikah*gajiPokok) + (tunjanganAnak*gajiPokok)
    p = 1.5
    potongan = (p/100) * gajiPokok
    gajiBersih = gajiKotor - potongan
elif gol == "D":
    gajiPokok = 5500000
    gajiKotor = gajiPokok + (tunjanganNikah*gajiPokok) + (tunjanganAnak *gajiPokok)
    p = 1
    potongan = (p/100) * gajiPokok
    gajiBersih = gajiKotor - potongan

tunjanganN = (tunjanganNikah*gajiPokok)
tunjanganA = (tunjanganAnak *gajiPokok)

#Menampilkan output
    
print("=" * 50)
print("STRUCK RINCIAN GAJI KARYAWAN")
print("_" * 50)

print(" Nama Karyawan : ", name,)
print(" Golongan : ", gol,)
if status == 1 :
    print("Status Pernikahan : Menikah")
    if jmlAnak != 0 and jmlAnak > 0 :
        print("Jumlah Anak : ", jmlAnak, )
if status == 0 :
    print("Status Pernikahan : Belum Menikah/Lajang")
    

print("-" * 50)
print(" Gaji Pokok : Rp", gajiPokok,)
if status == 1 :
    print("Tunjangan Nikah (", tN ,"%)"" : Rp", tunjanganN)
    if jmlAnak>0 :
        print("Tunjangan Anak (", tA*jmlAnak, "%)"" : Rp", tunjanganA)
print("="*50)
print("Gaji Kotor : Rp", gajiKotor,)
print(" Potongan " "(", p , "%)" " = Rp", potongan,)
print("-" * 50)
print(" Gaji Bersih : Rp", gajiBersih,)
