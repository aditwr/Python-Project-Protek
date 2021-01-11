file = open(r"d:\daftarPeminjam.txt", "w")
file.close()

file = open(r"d:\daftarPeminjam.txt", "a+")
""" input data """
import datetime
todaysdate = datetime.date.today()
today = str(todaysdate)
from datetime import timedelta, date
maxdate = todaysdate + timedelta(days = 7)
deadline = maxdate
repeat = "y"
print("""====================================
    PEMINJAMAN BUKU PERPUSTAKAAN
------------------------------------""")
while repeat == "y" or repeat == "Y" : 
    memberCode = str(input("Masukan kode member : "))
    memberName = str(input("Masukan nama member : "))
    title = str(input("Masukan judul buku : "))
    repeat = str(input("Ulangi lagi (y/n)"))

    file.write(memberCode+"|"+ memberName+"|"+title+"|"+today+"|"+str(deadline)+"|\n")
    
    if repeat == "n" or repeat == "no" or repeat == "NO" or repeat == "N" :
        break
    elif repeat == "y" or repeat == "Y":
        print("Masukan lagi!")
        continue
file.seek(0, 0)
data = file.read()
""" Output : membaca isi file daftarPeminjam.txt dan menampilkanya """
print("""
    Isi File : """)
print(data)
print("====================================")
""" menutup file """
file.close()


