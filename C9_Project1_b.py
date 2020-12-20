def ubahHuruf(teks, a, b) :
    teks = list(teks)
    for i in range (len(teks)) :
        if teks[i] == a :
            teks[i] = b
    hasil = "".join(teks)
    print(hasil)

ubahHuruf("MATEMATIKA", "A", "I")    
