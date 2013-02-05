#837799
def sequence(n):
    suite = 0
    while(n>1):
        if n%2==0:
            n=n/2
            suite+=1
        else:
            n=n*3+1
            suite+=1
    return suite



small=0
for a in reversed(range(1,1000000)):
    some = sequence(a)
    if some>small:
        small = some
        number=a
        print number
        print small
print number
print small

