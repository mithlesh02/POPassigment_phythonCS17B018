import random
def random_select(L,K,L1):
    for i in range(K):
        L1.append(random.choice(L))
L=['a','a','r','a','b','c','f','a','p','d','h','t','j','e']
L1=[]
random_select(L,3,L1)
print(L1)