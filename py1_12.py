def unpack(L,Y):
    for ele in L:
        for i in range(ele[0]):
            Y.append(ele[1])
L=[[4,'a'],[3,'b']]
Y=[]
unpack(L,Y)
print(Y)