def checkprime(n):
    if n==2 or n==3:
     return 'Yes'
    else :
        for i in range(2,n//2+1):
            if n%i==0:
                return 'No'
    return 'Yes'
k=checkprime(10)
print(k)
