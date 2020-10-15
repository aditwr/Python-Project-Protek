#program menghitung tarif rental

tarifPer12jam = 200000
tarifPerjam = 10000
jamMulai = 6
jamSelesai = 23
menitMulai = 0
menitSelesai = 50
jamSewa = (jamSelesai-jamMulai)
jamSewaMenitTambahan = ((menitSelesai-menitMulai)/60)
#jam : 17 jam
#menit : 50 menit/ 50/60 jam / 5/6 jam
HargaJamSewaUtama = (jamSewa//12)*200000
HargaJamSewaTambahan1 = (jamSewa%12)*10000
HargaJamSewaTambahan2 = (jamSewaMenitTambahan*10000)
TotalTarif = int(HargaJamSewaUtama+HargaJamSewaTambahan1+HargaJamSewaTambahan2)

print('Total tarif yang harus dibayarkan kepada rental mobil adalah Rp', TotalTarif, )

