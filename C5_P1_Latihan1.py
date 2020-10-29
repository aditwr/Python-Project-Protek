#Aplikasi untuk menentukan kelulusan Mahasiswa berdasarkan data Input

import time
#input data nilai
print("Selamat datang di Aplikasi")
print("Loading...")
time.sleep (3)
print("Silahkan masukan data nilai Mahasiswa..")
#nama mapel
print("Bahasa Indonesia = ...")
indo = int(input())

while indo >=0 or indo <0 :
    if indo >=0 and indo <=100 :
        print("Siahkan Masukan nilai Mapel Berikutnya..")
        print("Ilmu Pengetahuan Alam =...")
        break
    else :
        print("Nilai yang Anda masukan harus antara 0 - 100")
        time.sleep (2)
        print("Masukan Ulang nilai Mapel")
        print("Bahasa Indonesia")
        indo = int(input())
        if indo >=0 and indo <=100 :
            print("Silahkan masukan nilai Mapel berikutnya..")
            print("Ilmu Pengetahun Alam =...")
            break
        else :
            continue

ipa = int(input())
while ipa >=0 or ipa <0 :
    if ipa >=0 and ipa <=100 :
        print("Siahkan Masukan nilai Mapel Berikutnya..")
        print("Matematika =...")
        break
    else :
        print("Nilai yang Anda masukan harus antara 0 - 100")
        time.sleep (2)
        print("Masukan Ulang nilai Mapel")
        print("Ilmu Pengetahuan Alam =...")
        ipa = int(input())
        if ipa >=0 and ipa <=100 :
            print("Silahkan masukan nilai Mapel berikutnya..")
            print("Matematika =...")
            break
        else :
            continue

mtk = int(input())
while mtk >= 0 or mtk <0 :
    if mtk >=0 and mtk <=100 :
        print("Nilai mapel berhasil di input")
        break
    else :
        print("Nilai yang anda masukan harus antara nilai 1 - 100")
        time.sleep (2)
        print("Masukan ulang nilai Mapel")
        print("Matematika =...")
        mtk = int(input())
        if mtk >=0 and mtk <=100 :
              print("Nilai mapel berhasil diinput")
              break
        else :
            continue

time.sleep (3)
print("Menentukan Kelulusan")
print("Loading...")
time.sleep (3)

#Tampilkan data nilai di output
print("Daftar Nilai")
print("Bahasa Indonesia = ", indo)
print("Ilmu Pengetahuan Umum = ", ipa)
print("Matematika = ", mtk)

print("Status Kelulusan : ") 
if indo >=60 and ipa >=60 and mtk >70 :
    print("LULUS")
else :
    print("TIDAK LULUS")
