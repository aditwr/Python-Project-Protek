def shuffleString(string, n) :
    """ fungsi ini mnegacak string sebanyak n """
    import random
    resultList = []
    i = 1
    while i <= n :
        string = str(string)
        slist = list(string)
        random.shuffle(slist)
        result1= "".join(slist)
        if result1 in resultList :
            i = i - 1
            continue
        else :
            resultList.append(result1)
        i += 1
        
    print(resultList)

shuffleString("aditya", 10)
