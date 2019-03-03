def dupli(L,k,Y):
    for i in L:
        for _ in range(k):
          Y.append(i)
Y=[]
L=[1,2,3,4,5]
K=3
dupli(L,K,Y)
print(Y)

