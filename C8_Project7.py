daftarBuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

def hargaMax(data) :
    harga = list(data.values()) 
    buah = list(data.keys())
    return buah[harga.index(max(harga))]

print(hargaMax(daftarBuah))
