#Program Game Tebakan Angka Acak range 0 - 100

import time
from random import randint

print('=' * 50)
print("Welcome to Our Game :) ")
print('_' * 50)
time.sleep (2)
while True : 
    print("Hai, saya Mr. Leppie (*_*). Saya sudah memilih bilangan bulat secara random dari angka 0 - 100.")
    print("Ayo coba tebak, angka berapakah itu?")
    print("-" * 50)

    bil = randint(0, 100)

    time.sleep (2)
    score = 100
    print("Masukan angka tebakanmu :) ...")
    time.sleep (1)
    while True :
        print("Angka Tebakan : ...")
        n = int(input())
        if score <0 :
            print("Maaf anda gagal menyelesaikan Permainan Tebak Angka ini :(")
            break
        if n < bil :
            print("Hehehe... Bilangan tebakan anda terlalu kecil")
            print("Masukan angka Tebakan lagi")
            score = score - 50
            continue
        if n > bil :
            print("Hehehe... Bilangan tebakan anda terlalu besar")
            print("Masukan angka Tebakan lagi")
            score = score - 50
            continue
        if n == bil :
            print("Yeee... Bilangan Tebakan Anda BENAR ;) ")
            break

    print("="*50)
    if score >= 0 :
        print("Score anda : " + str(score))
    else :
        print("Anda gagal, Apakah anda mau mengulagi permainan? (yes/no)")
        acc = input()

    if acc == "yes":
        continue
    elif acc == "no" :
        print("Terimakasih sudah Bermain :)")
        time.sleep (2)
        print("Closing the Game")
        break
    else :
        print("Masukan Anda SALAH")
        print("Program akan terhenti")
        break
