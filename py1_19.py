def rotate(L,k,L1):
    for i in range(k,len(L)):
        L1.append(L[i])
    for j in range(k):
        L1.append(L[j])
L=['a','a','r','a','b','c','f','a','p','d','h','t','j','e']
L1=[]
rotate(L,3,L1)
print(L1)