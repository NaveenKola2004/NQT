def largest_num(l):
    n=len(l)
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if(l[j]<l[j+1]): #for (l[j]>l[j+1]) -> for lowest number
                temp=l[j]
                l[j]=l[j+1]
                l[j+1]=temp
    return l
l=[]
n=int(input())
for i in range(0,n):
    k=int(input())
    l.append(k)
print(largest_num(l)[0])
