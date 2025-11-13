def Max_min(n):
    l=[]
    while(n>0):
        digit=n%10
        l.append(digit)
        n//=10
    return max(l),min(l)
n=int(input())
print(Max_min(n))