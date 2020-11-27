#program untuk membuka file dengan suppport append (a)
#menambhakan data pada file yang telah dibuka


akses = "y"
while akses == "y" :
    try :
        aksesFile = str(input("Masukan lokasi, nama, dan ekstensi file: "))
        file = open(aksesFile, "a")
        dataInput = input("Masukan data yang ingin di input : ")
        file.write(dataInput)
        file = open(aksesFile, "r")
        print(file.read())
        file.close()
    except FileNotFoundError :
        print("identitas file salah, masukan lagi5")
        continue
    akses = str(input("Ingin menambahkan data lagi? (y/n)"))

    
