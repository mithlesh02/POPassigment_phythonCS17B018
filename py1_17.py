def split(L,K,L1,L2):
    for i in range(K):
        L1.append(L[i])
    for j in range(K,len(L)):
        L2.append(L[j])

L=['a','a','r','a','b','c','f','a','p','d','h','t','j','e']
L1=[]
L2=[]

split(L,3,L1,L2)
print(L1,L2)
