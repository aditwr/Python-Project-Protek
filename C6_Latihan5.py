def sum(*myData):
    #unit values
    sum  = 0
    i = 0
    #menjumlahkan semua data
    for data in myData :
        sum += data
        i += 1
    print(sum)

def average(*myData):
    #unit values
    sum = 0
    i = 0
    #mencari jumlah dan banyaknya data
    for data in myData :
        sum += data
        i += 1
        #mencari rata2
        average = sum/i
    print(average)

def maks(*data):
    hasil = max(data)
    print(hasil)

def minimum(*data):
    hasil = min(data)
    print(hasil)

#a
print("A. (5, 10, 4, 9, 30, 16, 2, 11)")
sum(5, 10, 4, 9, 30, 16, 2, 11)
average(5, 10, 4, 9, 30, 16, 2, 11)
maks(5, 10, 4, 9, 30, 16, 2, 11)
minimum(5, 10, 4, 9, 30, 16, 2, 11)
print("B. (81, 98, 12, 83, 45, 77, 69, 30, 56)")
#b
sum(81, 98, 12, 83, 45, 77, 69, 30, 56)
average(81, 98, 12, 83, 45, 77, 69, 30, 56)
maks(81, 98, 12, 83, 45, 77, 69, 30, 56)
minimum(81, 98, 12, 83, 45, 77, 69, 30, 56)
