a = [1, 5, 6, 3, 6, 9, 11, 20, 12]
b = [7, 4, 5, 6, 7, 1, 12, 5, 9] 

c = a[0:8]
d = b[2:10] 

e = []
d.append(0)
for i in range (len(c)) : 
    e.append(c[i] + d[i])
        

print("c = ", c)
print("d = ", d)
print("e = ", e)
    



