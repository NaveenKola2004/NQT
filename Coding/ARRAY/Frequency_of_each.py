# Method 1
def Fun(n):
    k={}
    for i in range(len(n)):
        if n[i] not in k:
            k[n[i]]=1
        else:
            k[n[i]]+=1
    for i in k:
        print(f"{i} : {k[i]}")
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
Fun(l)
