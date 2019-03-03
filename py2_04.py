def checkprime(n):
    if n==2 or n==3:
     return 'Yes'
    else :
        for i in range(2,n//2+1):
            if n%i==0:
                return 'No'
    return 'Yes'

def ranges(i,k,L):
    for i in range(i,k+1):
        if checkprime(i)=='Yes':
            L.append(i)


L=[]
ranges(3,100,L)
print(L)
