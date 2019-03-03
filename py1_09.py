def pack(L,Y):
    r=0
    for i in range(len(L)):
        if L[r]!=L[i]:
            Y.append(L[r:i])
            r=i
        elif i==len(L)-1:
            Y.append(L[r:i+1])
            r=i
L=['a','a','a','a','b','b','b','a','a','d','d','t','t','e','e']
Y=[]
pack(L,Y)
print(Y)
