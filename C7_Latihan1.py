try :
    #input nama file untuk variabel namaFile
    namaFile = str(input("Masukan nama File : "))
    #perintah open
    isiFile = open(str(namaFile), "r")
    print(isiFile.read())
except ValueError :
    print("nama file harus berupa string dan mengandung patch, nama dan elstensi file")
except FileNotFoundError :
    print("File tidak ditemukan")
