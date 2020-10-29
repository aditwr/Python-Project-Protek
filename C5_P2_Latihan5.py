#Program Game Tebakan Angka Acak range 0 - 100

import time
from random import randint

print('=' * 50)
print("Welcome to Our Game :) ")
print('_' * 50)
time.sleep (2)
print("Hai, saya Mr. Leppie (*_*). Saya sudah memilih bilangan bulat secara random dari angka 0 - 100.")
print("Ayo coba tebak, angka berapakah itu?")
print("-" * 50)

bil = randint(0, 100)

time.sleep (2)

print("Masukan angka tebakanmu :) ...")
time.sleep (1)

while True :
    print("Angka Tebakan : ...")
    n = int(input())
    if n < bil :
        print("Hehehe... Bilangan tebakan anda terlalu kecil")
        print("Masukan angka Tebakan lagi")
        continue
    if n > bil :
        print("Hehehe... Bilangan tebakan anda terlalu besar")
        print("Masukan angka Tebakan lagi")
        continue
    if n == bil :
        print("Yeee... Bilangan Tebakan Anda BENAR ;) ")
        break
        
    
