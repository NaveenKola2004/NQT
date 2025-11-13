def GP(a,r,n):
    l=[]
    l.append(a)
    for i in range(n-1):
        a=a*r
        l.append(a)
    sum=0
    for i in l:
        sum+=i
    return sum
a=int(input())
r=int(input())
n=int(input())
print(GP(a,r,n))