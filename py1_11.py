def pack(L,Y):
    r=0
    for i in range(len(L)):
        if L[r]!=L[i]:
            if i-r==1:
              Y.append(L[r])
              r=i
            else:
             Y.append([i-r,L[r]])
             r=i
        elif i==len(L)-1:
            if i+1-r==1:
               Y.append(L[r])
               r=i
            else:
             Y.append([i+1-r,L[r]])
             r=i
L=['a','a','a','a','w','b','b','a','a','d','d','t','t','r','e']
Y=[]
pack(L,Y)
print(Y)
