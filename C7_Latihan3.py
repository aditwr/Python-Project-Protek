print("-" * 50)
print("PROGRAM HITUNG RATA-RATA")
print("-" * 50)

access = "y"
sum = 0
n = 0
while access == "y" :
    try :
        bil = int(input("Masukan Bilangan Bulat : "))
        sum = sum + bil
        n = n + 1
        access = str(input("Lagi? (y/n)"))
    except ValueError :
        print("Bukan bilangan Bulat")
        continue


rata2 = sum/n
print("-" * 50) 
print("Rata-ratanya adalah : ", rata2)
print("-" * 50)
