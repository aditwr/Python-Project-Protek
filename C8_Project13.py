nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	    {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

listNama = []
listNim = []
listMid = []
listUas = []
listHasil = []

for i in range (len(nilaiMhs)) :
    mid = (nilaiMhs[i])['mid']
    uas = (nilaiMhs[i])['uas']
    nim = (nilaiMhs[i])['nim']
    nama = (nilaiMhs[i])['nama']
    listMid.append(mid)
    listUas.append(uas)
    listNama.append(nama)
    listNim.append(nim)

def maxNilai(nilaiMid, nilaiUas) :
    hasil = (nilaiMid + (nilaiUas*2))/3
    listHasil.append(hasil)

for i in range (len(listNama)) :
    maxNilai(listMid[i], listUas[i])

print("Mahasiswa dengan nilai tertinggi : ")
print()
print(" NIM = ", listNim[listHasil.index(max(listHasil))],
      ", Nama = ", listNama[listHasil.index(max(listHasil))])
    


    
