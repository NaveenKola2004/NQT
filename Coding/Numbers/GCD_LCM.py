def GCD_LCM(a,b):
    l1=set()
    l2=set()

    for i in range(1,a+1):
        if a%i==0:
            l1.add(i)
    for i in range(1,b+1):
        if b%i==0:
            l2.add(i)
    GCD=max(l1.intersection(l2))
    LCM=(a*b)//GCD
    print(f"GCD : {GCD}\nLCM : {LCM}")
GCD_LCM(12,18)