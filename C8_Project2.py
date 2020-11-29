x = [10, 5, 20, 5]


def dataStat(x) :
    data = tuple(x)
    listHasil = []
    nilaiMaks = max(data)
    nilaiMin = min(data)
    n = len(data)
    jumlahData = sum(data)
    rata2 = jumlahData/n
    rata2 = round(rata2, 2)
    listHasil.append(rata2)
    listHasil.append(nilaiMaks)
    listHasil.append(nilaiMin)
    return listHasil
    
print(dataStat(x))  
