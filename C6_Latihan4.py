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
    
   


      
