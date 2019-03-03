import random
def creat(L,K,J):
    for i in range(K,J+1):
        L.append(i)

def random_select(L,K,L1):
    for i in range(K):
        L1.append(random.choice(L))
L=[]
creat(L,3,9)
L1=[]
random_select(L,3,L1)
print(L1)