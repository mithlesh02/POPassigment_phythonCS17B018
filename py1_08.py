L=['a','a','a','a','b','c','c','a','a','d','e','e','e','e']
out=[]
p=L[0]
out.append(p)
for i in range(1,len(L)):
    if p!=L[i]:
        out.append(L[i])
        p=L[i]

print(out)