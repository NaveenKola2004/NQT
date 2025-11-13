def Leap(n):
    if n%400==0:
        return True
    elif n%100==0:
        return False
    elif n%4==0:
        return True
    else:
        return False
n=int(input())
if Leap(n):
    print("Leap Year")
else:
    print("Not Leap Year")