def Number_poli(n):
    reverse=0
    origonal=n
    while (n>0):
        digit=n%10
        reverse=(reverse*10)+digit
        n=n//10
    if reverse==origonal:
        return "Yes"
    else:
        return "NO"
n=int(input())
print(Number_poli(n))