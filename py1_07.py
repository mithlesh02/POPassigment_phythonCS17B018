L=['a', ['b', ['c', 'd'], 'e']]
Out=[]

def flatten(L):
    for i in L:
        if type(i)==list:
            flatten(i)
        else :
            Out.append(i)

print('The original list = ',L)
flatten(L)
print('The list after flatting',Out)