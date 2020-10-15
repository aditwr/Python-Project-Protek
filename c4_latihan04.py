#program menghitung waktu tiba di kota C tanpa "input"

jamBerangkat = 6
s1 = 125
v1 = 62
isti = 45
s2 = 256
v2 = 70

t1 = round(s1/v1)
t2 = round(s2/v2)
waktuPerjalanan = t1 + t2
waktuTiba = jamBerangkat + waktuPerjalanan
print("Waktu saat tiba di kota C adalah pukul", waktuTiba, '.' , isti,)



#program Menghitung waktu tiba di C dengan "input"


jamBerangkat = b = int(input("Masukan angka jam Berangkat"))
s1 = int(input("Masukan jarak antara Kota A dan B")) #125
v1 = int(input("Masukan kecepatan rata-rata dari kota A menuju kota B")) #62
isti = int(input("Masukan banyak menit istirahat")) #45
s2 = int(input("Masukan jarak kota B dengan kota C")) #256
v2 = int(input("Maukan kecepatan rata-rata dari kota B ke kota C")) #70


t1 = round(s1/v1)
t2 = round(s2/v2)
waktuPerjalanan = t1 + t2
waktuTiba = jamBerangkat + waktuPerjalanan
print("Waktu saat tiba di kota C adalah pukul", waktuTiba, '.' , isti,)
