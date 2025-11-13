def Ap(n,start,diff):
    l1=[]
    for _ in range(n):
        l1.append(start)
        start=start+diff
    sum=0
    for i in l1:
        sum=sum+i
    return(sum)
n=int(input())
s=int(input())
d=int(input())
print(Ap(n,s,d))