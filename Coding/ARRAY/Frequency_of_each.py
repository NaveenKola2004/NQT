def frequency(l):
    n=len(l)
    visted=[False]*n
    for i in range(n):
        if visted[i]==True:
            continue
        count=1
        for j in range(i+1,n):
            if l[i]==l[j]:
                visted[j]=True
                count+=1
        print(l[i],count)
l=[]
n=int(input())
for _ in range(n):
    l.append(int(input()))
frequency(l)