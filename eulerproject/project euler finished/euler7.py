import math
def isPrime(n):
    i = 2
    sqrtN = math.sqrt(n)
    while i<=sqrtN:
        if n%i==0:
            return " "
        i+=1
    return n

i=2
numberOfPrime=0
while(1):
    if numberOfPrime==10001:
        break
    some = isPrime(i)
    if some!=' ':
        print some
        numberOfPrime+=1
    i+=1
