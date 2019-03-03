def insert(data,L,k,L1):
    for i in range(len(L)):
        if i!=k-1:
         L1.append(L[i])
        else:
          L1.append(data)
          L1.append(L[i])
L=['a','a','r','a','b','c','f','a','p','d','h','t','j','e']
L1=[]
data='alpha'
insert(data,L,3,L1)
print(L1)