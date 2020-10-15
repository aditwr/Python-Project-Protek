#jarak 795km
#setiap 12 km butuh 1 liter
#kapasitasTangki 50 liter

import time
print("Aplikasi untuk memperkirakan Banyaknya anda harus mengisi bensin saat perjalanan")

#jeda 3 detik
time.sleep(3)

#input jarak perjalanan
jarak = int(input("Masukan jarak perjalanan Anda...km")) 


#input jarak tempuh apabila menggunakan 1 liter
satuLtBensin = int(input("Masukan jarak yang dapat ditempuh setiap penggunaan bensin 1 liter...km"))

#input kapasitas tangki mobil
kapasTangki = int(input("Masukan kapasitas tangki kendaraan Anda...liter"))

#menghitung kebutuhan bensin
butuhBensin = round((jarak/satuLtBensin), 3)

#menghitung banyak minimal n kali mengisi bensin
banyakMinIsiBensin = butuhBensin//kapasTangki

#jeda 3 detik
time.sleep(3)

#menampilkan hasil
print('Anda harus mengisi Bensin minimal ', banyakMinIsiBensin , 'kali')

#jeda 2 detik
time.sleep(2)

#print kata penutup
print("Semoga perjalanan Anda menyenangkan... :)")

#jarak = 795
#kapasitasTangki = 50
#satuLtBensin = 12
