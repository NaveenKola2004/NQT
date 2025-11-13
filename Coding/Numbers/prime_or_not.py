def Prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())

if Prime(n):
    print("prime")
else:
    print("Not")

    # in a range primes

    for i in range(2,n+1):
        if Prime(i):
            print(i)