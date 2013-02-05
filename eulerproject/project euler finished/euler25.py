a,b=1,1
numberofdigits=0
term=1
while numberofdigits!=1000:
    numberofdigits=0
    a,b = b,a+b
    term+=1
    for number in str(a):
            numberofdigits+=1
print term
