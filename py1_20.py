def rotate(L,k,L1):
    for i in range(len(L)):
        if i!=k-1:
         L1.append(L[i])
    
L=['a','a','r','a','b','c','f','a','p','d','h','t','j','e']
L1=[]
rotate(L,3,L1)
print(L1)