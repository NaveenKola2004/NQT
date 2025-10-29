def Descending_order(l):
    n=len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if (l[j]<l[j+1]):
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    return l
l=[]
n=int(input())
for _ in range(n):
    l.append(int(input()))
print(Descending_order(l))