def Reverse(n):
    l=len(n)
    for i in range(l//2):
        temp=n[l-i-1]
        n[l-i-1]=n[i]
        n[i]=temp
    return n
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
print(Reverse(l))