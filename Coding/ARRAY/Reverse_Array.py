def Reverse_Array(l):
    n=len(l)
    for i in range(n//2):
        temp=l[i]
        l[i]=l[n-i-1]
        l[n-i-1]=temp
    return l
l=[]
n=int(input())
for i in range(n):
    l.append(int(input()))
print(Reverse_Array(l))