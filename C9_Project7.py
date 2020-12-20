mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
nim = []
nama = []
tgl = []
alamat = []
for i in range(len(mhs)) :
    daftar = mhs[i].split(":")
    nim.append(daftar[0])
    nama.append(daftar[1])
    alamat.append(daftar[3])
    tl = daftar[2].split("-")
    tanggal = []
    tanggal.append(tl[2])
    tanggal.append(tl[1])
    tanggal.append(tl[0])
    tanggal = "/".join(tanggal)
    tgl.append(tanggal)

print("""
========================================================================
NIM	   NAMA MAHASISWA	   TGL LAHIR	   TEMPAT LAHIR
------------------------------------------------------------------------""")
for i in range (len(mhs)) :
    print(nim[i].ljust(10), nama[i].ljust(23), tgl[i].ljust(15)
          , alamat[i])
print("""------------------------------------------------------------------------""")
