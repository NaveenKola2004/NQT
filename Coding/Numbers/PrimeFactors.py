# Print all Prime Factors of the given number

def Prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def Factors(n):
    l=[]
    for i in range(2,n+1):
        if n%i==0:
            if Prime(i):
                l.append(i)
    return l
n=int(input())
print(Factors(n))