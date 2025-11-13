def Armstrong_number(n):
    count=0
    store=n
    sum=0
    temp=n
    while (n>0):
        digit=n%10
        count+=1
        n=n//10
    while (temp>0):
        digit=temp%10
        k=digit**count
        sum+=k
        temp=temp//10
    if sum==store:
        return "Yes"
    else:
        return "NO"
n=int(input())
print(Armstrong_number(n))