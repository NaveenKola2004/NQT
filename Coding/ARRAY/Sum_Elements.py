def Sum_Elements(l):
    sum=0
    for i in l:
        sum+=i
    return sum
l=[]
n=int(input())

for _ in range(n):
    l.append(int(input()))
print(Sum_Elements(l))