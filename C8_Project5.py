bil = [1, 2, 3, 4, 5]

def kuadrat(bil) :
    data = []
    for i in range (len(bil)) :
        value = (bil[i]**2)
        data.append(value)
    print(data)

kuadrat(bil)
