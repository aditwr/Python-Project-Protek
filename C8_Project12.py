#database
daftarBuah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

akses = "y"
while akses == "y" :
    print('MENU UTAMA : ')
    print()
    print("A. Tambah data Buah ")
    print("B. Beli Buah ")
    print("C. Hapus data Buah")
    print()

    while True :
        access = str(input("Pilihan anda : "))
        if access != "A" and access != "a" and access != "B" and access != "b" and access != "C" and access != "c" :
            print('input salah, Masukan ulang')
            continue
        else :
            break

    if access == "A" or access == "a" :
        print("Menambahkan Data...")
        acc = "y"
        while acc == "y" :
            buah = str(input("Masukan nama buah : "))
            if buah not in daftarBuah :
                harga = int(input("Masukan harga satuan : "))
                daftarBuah[buah] = harga
            else :
                print('Nama buah sudah ada di dalam dictionary')
                
            
            namaBuah = list(daftarBuah.keys())
            hargaBuah = list(daftarBuah.values())
            print("Data Buah : ")
            for i in range (len(namaBuah)) :
                print((i+1, str(namaBuah[i]),'(Harga Rp', str(hargaBuah[i])))
            acc = str(input("Tambahkan lagi? (y/n)"))


    if access == "B" or access == "b" :
        print("Pembelian Buah...")
        acc = "y"
        totalHarga = 0
        while acc == "y" :
            buah = str(input('Nama buah yang dibeli : '))
            kg = int(input('Berapa Kg :'))
            
            harga = (daftarBuah[buah]) * kg
            totalHarga = totalHarga + harga
            acc = str(input("Beli buah yang lain? (y/n)"))

        print( '-' * 30)
        print('Total Harga : ', totalHarga)

    if access == "C" or access == "c" :
        print("Menghapus data Buah...")
        acc = "y"
        while acc == "y" :
            buah = str(input("Masukan nama buah yang akan dihapus : "))
            if buah in daftarBuah :
                del daftarBuah[buah]
                print("data buah ", buah, " berhasil di hapus")
            elif buah not in daftarBuah :
                print("data buah ", buah, " tidak ditemukan!") 

            namaBuah = list(daftarBuah.keys())
            hargaBuah = list(daftarBuah.values())
            print("Data Buah : ")
            for i in range (len(namaBuah)) :
                print((i+1, str(namaBuah[i]),'(Harga Rp', str(hargaBuah[i])))
            acc = str(input("Hapus lagi? (y/n)"))
            
    
    while True :
        print()
        akses = str(input('Kembali ke menu utama? (y/n)'))
        if akses == "y" :
            global aksesMenu
            aksesMenu = "y"
            break
        elif akses == "n" :
            import sys
            sys.exit()
        elif akses != "y" and akses!= "n" :
            print("input salah, input harus huruf 'y' atau 'n' ")
            print('mohon masukan ulang input')
            continue
    
    akses = aksesMenu

    
