# 1 1. Unique elements from numbers:

### Hear is the sample code in python 👇👇

```python
def Frequncy(n):
    max=0
    for i in n:
        if i>max:
            max=i
    c=[0]*(max+1)
    for i in n:
        c[i]+=1
    return c

l=[1,2,3,4,2,1,33,9]
re=Frequncy(l)
for i in range(len(re)):
    if re[i]==1:
        print(i)
```