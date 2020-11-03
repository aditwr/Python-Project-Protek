#function membuat formasi star sesuai varibael n
def starFormation(n):
    n = n
    i = 0
    z = 1
    while i < n :
        print("* " * z)
        i += 1
        z += 1



#starFormation2
def starFormation2(n):
    n = z
    i = 0
    while i < n:
        print("* " * z)
        i += 1
        z -= 1

#starFormation Gabungan
def starFormation3(n):
    n = n
    i = 0
    z = 1
    if n%2 == 0 :
        while i < n/2 :
            print("* " * z)
            i += 1
            if i != n/2 :
                z += 1
            elif i == n/2 :
                z = z
            z = z
        while i >= n/2 and i <n :
            print("* " * z)
            i += 1
            z -= 1
    if n%2 == 1 :
        while i < (n+1)/2 :
            print("* " * z)
            i += 1
            if i != (n+1)/2 :
                z += 1
            elif i == (n+1)/2 :
                z -= 1
            z = z
        while i >= (n+1)/2 and i< n:
            print("* " * z)
            i += 1
            z -= 1

starFormation3(7)
starFormation3(8)
        
        
       
            
