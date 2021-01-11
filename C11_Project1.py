#FUNCTION : difference day between two dates
def diffDate(x) :
    from datetime import datetime
    now = datetime.date(datetime.today())
    future = datetime.strptime(x, "%Y-%m-%d").date()
    diff = (future - now).days
    return diff

#program
from datetime import datetime
dateNow = datetime.date(datetime.now())
print(""" Cek Selisih Hari antara hari ini dengan tanggal yang anda tentukan
----------------------------------------------------""")
print("Tanggal hari ini : ", dateNow)
print()
dateFuture = str(input(""" Format : YYYY-MM-DD
Masukan Tanggal di masa depan : """))
x = dateFuture
print("""
Hasil : """, end='')
#MEMANGGIL FUNGSI diffDate(x)
hasil = diffDate(x)
print(hasil, "Hari")
#
if hasil >0 :
    print("Masih ada ", hasil, "hari lagi :), tenanglah")
elif hasil < 0 :
    print("Maaf tanggal itu sudah terlewati :( , ", hasil, "hari sebelumnya")
elif hasil == 0 :
    print("Itu hari ini Bungg :)")




