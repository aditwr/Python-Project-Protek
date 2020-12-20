def bintang(n) :
    n1 = int((n+1)/2)
    
    if (n+1)%2 == 0 :
        a = 1
        for i in range (1, n1) :
            print(("*" * a).center(50))
            a += 2
        
        for i in range (n1, int(n+1)) :
            print(("*" * a).center(50))
            a -= 2

    else :
        print("""Argumen "n" pada function "bintang(n)" harus berupa
Bilangan Ganjil. """)
            
bintang(8)
