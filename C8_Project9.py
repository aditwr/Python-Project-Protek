Nama buah yang dibeli 	: XXXX
Berapa Kg		: XXXX
-------------------------------------------
Total harga		: XXXX

daftarBuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

buah = str(input('Nama buah yang dibeli : '))
kg = int(input('Berapa Kg :'))

totalHarga = (daftarBuah[buah]) * kg
print( '-' * 30)
print('Total Harga : ', totalHarga)
