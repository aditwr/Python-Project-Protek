daftarSayur = ["bayam", "kangkung", "wortel", "selada"]

akses = "y"
while akses == "y" :
    print('MENU UTAMA : ')
    print("mengolah data sayur : " )
    print()
    print("A. Tambah data sayur ")
    print("B. Hapus data sayur ")
    print("C. Tampilkan data sayur")
    print()

    while True :
        access = str(input("Pilihan anda : "))
        if access != "A" and access != "a" and access != "B" and access != "b" and access != "C" and access != "c" :
            print('input salah, Masukan ulang')
            continue
        else :
            break

    if access == "A" or access == "a" :
        print("Menambah data sayur...")
        acc = "y"
        while acc == "y" :
            sayur = str(input("Masukan nama sayur yang akan ditambahkan : "))
            daftarSayur.append(sayur)
            acc = str(input("Tambahkan lagi? (y/n)"))

    if access == "B" or access == "b" :
        print("Menghapus data sayur...")
        acc = "y"
        while acc == "y" :
            sayur = str(input("Masukan nama sayur yang akan dihapus dari daftar :"))
            if sayur in daftarSayur :
                daftarSayur.remove(sayur)
                print("sayur ", sayur, " telah dihapus dari daftar")
            if sayur not in daftarSayur :
                print("sayur ", sayur, " tidak ditemukan di dalam daftar")
            acc = str(input("Menghapus lagi? (y/n)"))

    if access == "C" or access == "c" :
        print('Menampilkan daftar sayur saat ini : ')
        for i in range (len(daftarSayur)) :
            print(i+1, ". ", daftarSayur[i])
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
