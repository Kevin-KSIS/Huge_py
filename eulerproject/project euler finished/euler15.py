def fact(n):
    some=1
    for a in range(1,n+1):
        some*=a
    return some
n=20
answer=fact(2*n)/(fact(n)*fact(n))
print answer
