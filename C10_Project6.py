""" enkripsi teks atau string dengan sandi caesar """

string = str(input("Masukan Teks yang akan dienkripsi (dalam KAPITAL) : "))
change = int(input("Masukan besar pergeseran kode ASCII : "))

enkripsi = ""

for char in string :
    if char == " " :
        karakter = " "
        enkripsi = enkripsi + karakter
    elif string.isupper() :
        charCode = ord(char)
        index = ord(char) - ord("A")
        newIndex = (index + change) % 26
        kode = newIndex + ord("A")
        karakter = chr(kode)

        enkripsi = enkripsi + karakter

print("TEKS ASLI : ", string)
print("TEKS TERENKRIPSI : ", enkripsi)
        
        
