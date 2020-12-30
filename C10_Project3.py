file = open(r"d:\dataMahasiswa.txt", "r")
daftar = {}
dataMhs = []

for line in file :
    nim, name, add = line.split("|")
    daftar = {"nim" : nim, "nama" : name, "alamat" : add}
    dataMhs.append(daftar)

print((dataMhs))
 




