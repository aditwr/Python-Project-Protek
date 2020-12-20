def ubahHuruf(teks, a, b) :
    teks = list(teks)
    for n, i in enumerate(teks) :
        if i == a :
            teks[n] = b
    hasil = "".join(teks)
    print(hasil)

ubahHuruf("MATEMATIKA", "A", "I")
