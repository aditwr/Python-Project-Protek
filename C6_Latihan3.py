#factorial function

def factorial(n):
    if n == 0 :
        return 1
    else :
        return n * factorial(n-1)

#C(5, 3)
Combinasi = factorial(5)/(factorial(3)*(factorial(5)-factorial(3)))
print("C(5, 3) = ", Combinasi)
#P(10, 7)
Permutasi = factorial(10)/(factorial(10)-factorial(7))
print("P(10, 7) = ", Permutasi)
