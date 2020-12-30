"""membuat file dan menulis file kosong """
file = open(r"d:\dataMhs.txt", "w+")
""" head """
print("""   DATA MAHASISWA
===================================""")

""" masukan input """
repeat = "y"
while repeat =="y" or repeat == "Y" :
    nim = str(input("Masukan NIM : "))
    name = str(input("Masukan nama : "))
    alamat = str(input("Masukan alamt : "))
    """ menuliskan input ke dalam file """
    file.write(nim+" | "+name+" | "+alamat+"\n")
    repeat = str(input("Ulangi ? (y/n))"))
    if repeat == "n" or repeat == "N" :
        break
    elif repeat == "y" or repeat == "Y" :
        print("Masukan lagi!")
        continue
file.seek(0, 0)
data = file.read()
""" output """
print("""===================================
    DATA
-----------------------------------""")
print(data)
print("-----------------------------------")

"""menutup file """


file.close()
