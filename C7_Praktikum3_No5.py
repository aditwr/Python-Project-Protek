#c7_praktikum no 5
try :
    #membuka file
    file = open("d:/data.txt", "r")
    
    bil1 = int(file.readline())
    bil2 = int(file.readline())
    hasil = bil1/bil2
    print(bil1, ' dibagi ', bil2, ' sama dengan ', hasil)

except ZeroDivisionError :
    print("Tidak boleh Pembagian dengan nol")
except FileNotFoundError :
    print("File tidak ditemukan")
