#1)a for loop to 999
#2)another one to 999
#3)another one inside the other to 999
#inside 3) check all 1)+2)+3) == 1000
#now I have all the possible combinaisons
#now try a**2 + b**2 ==c**2
#find a,b & c
#a=200, b=375, c=425
for a in range(1,999):
    for b in range(1,999):
        for c in range(1,999):
            some=a+b+c
            if some==1000 and a*a+b*b==c*c:
                print "a="+str(a)+", b="+str(b)+", c="+str(c)
