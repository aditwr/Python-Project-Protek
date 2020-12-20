""" fungsi untuk membuat segitiga dari bintang dengan n = banyak baris """

def bintang(n):
    a = 1
    for i in range (n) :
        print(("*" * a).center(50))
        a += 2

bintang(10)

