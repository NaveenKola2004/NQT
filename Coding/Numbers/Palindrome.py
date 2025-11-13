def palindrome(n):
    rev=0
    while n>0:
        digit=n%10
        rev=(rev*10)+digit
        n//=10
    return rev
n=int(input())
if n==palindrome(n):
    print("YES")
else:
    print("NO")

    # in a range polindromes

    for i in range(11,n+1):
        if i==palindrome(i):
            print(i)