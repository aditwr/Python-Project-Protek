daftarBuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

def rataHarga(data) :
    harga = list(data.values())
    rata2 = (sum(harga))/(len(harga))
    return rata2

print(rataHarga(daftarBuah))
