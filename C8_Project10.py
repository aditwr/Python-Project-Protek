daftarBuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

acc = "y"
totalHarga = 0
while acc == "y" :
    buah = str(input('Nama buah yang dibeli : '))
    kg = int(input('Berapa Kg :'))
    
    harga = (daftarBuah[buah]) * kg
    totalHarga = totalHarga + harga
    acc = str(input("Beli buah yang lain? (y/n)"))

print( '-' * 30)
print('Total Harga : ', totalHarga)
