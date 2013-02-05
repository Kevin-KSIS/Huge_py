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
sumofprimes=0
numberOfPrime=0
while(1):
    if i>2000000:
        break
    some = isPrime(i)
    if some!=' ':
        numberOfPrime+=1
        sumofprimes+=some
        print sumofprimes
    i+=1
