def pack(L,Y):
    r=0
    for i in range(len(L)):
        if L[r]!=L[i]:
            Y.append([i-r,L[r]])
            r=i
        elif i==len(L)-1:
            Y.append([i+1-r,L[r]])
            r=i
L=['a','a','a','a','b','b','b','a','a','d','d','t','t','e','e']
Y=[]
pack(L,Y)
print(Y)
