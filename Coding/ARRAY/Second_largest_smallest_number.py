def Second_largest(l):
    n=len(l)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if (l[j]<l[j+1]):
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    return l
l=[]
n=int(input())

for i in range(n):
    l.append(int(input()))
print(Second_largest(l)[1])