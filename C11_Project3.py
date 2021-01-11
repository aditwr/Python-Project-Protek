#baca file daftarPeminjam.txt
#tanggal pengembailian = date.today
#selisih tanggal dengan diffDate
def diffDate(x) :
    from datetime import datetime
    now = datetime.date(datetime.today())
    future = datetime.strptime(x, "%Y-%m-%d").date()
    diff = (future - now).days
    return diff
#baca file
file = open(r"d:\daftarPeminjam.txt", "r")
""" membaca isi file ke dict in dict """
data = {}
for line in file :
    kode, nama, judul, tglPinjam, tglDeadline, end = line.split("|")
    data[kode] = {"kode":kode, "nama":nama, "judul":judul, "tglPinjam":tglPinjam, "tglDeadline":tglDeadline}
#cek keterlamatan
from datetime import datetime
tglKembali = datetime.date(datetime.today())

#input
KODE = str(input("Masukan Kode Member : "))
#cek
try :
    Data = data[KODE]
    #cek keterlambatan4
    deadline = datetime.strptime(data[KODE]["tglDeadline"], "%Y-%m-%d").date()
    lateDay = (tglKembali - deadline).days
    if lateDay <= 0 :
        terlambat = ""
        Denda = ""
    elif lateDay > 0 :
        denda = int(lateDay)*2000
        Denda = "Rp" + str(denda)
        terlambat = str(lateDay) + " hari"
    #output    
    print("""   Data Peminjaman Buku """)
    print("Kode Member              : ", data[KODE]["kode"])
    print("Nama Member              : ", data[KODE]["nama"])
    print("Judul Buku               : ", data[KODE]["judul"])
    print("Tanggal Mulai Peminjaman : ", tglPinjam)
    print("Tanggal Maks Peminjaman  : ", tglDeadline)
    print("Tanggal Pengembalian     : ", tglKembali)
    print("Terlambat                : ", terlambat)
    print("Denda                    : ", Denda)
        
        
except KeyError :
    print("Data tidak Ditemukan!")
    
