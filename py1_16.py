def drop(L,k,Y):
    for i in range(1,len(L)+1):
        if i%k!=0:
          Y.append(L[i-1])
Y=[]
L=['a','a','r','a','b','c','f','a','p','d','h','t','j','e']
K=3
drop(L,K,Y)
print(Y)