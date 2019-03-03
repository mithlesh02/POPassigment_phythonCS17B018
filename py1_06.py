#L=[1,2,3,4,5,4,3,2,1]
L=["Tirupati","Delhi","Patna","Agra","Mumbai","Mumbai","Agra","Patna","Delhi","Tirupati"]
flag=0
for i in range(len(L)//2):
     if L[i]!=L[-i-1]:
        print("List is not a palindrome")
        flag=1
        break
if flag==0:
    print("List is a palindrome")