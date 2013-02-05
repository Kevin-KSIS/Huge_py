#first to sort:
#appendToFile = open("euler22file", "r")
#sortToFile = open("sortedFile", "w")
#for line in sorted(appendToFile, key = str.lower):
#    sortToFile.write(line)
def countpoints(mot):
    points=0
    for a in mot:
        if a=="A":
            points+=1
        if a=="B":
            points+=2
        if a=="C":
            points+=3
        if a=="D":
            points+=4
        if a=="E":
            points+=5
        if a=="F":
            points+=6
        if a=="G":
            points+=7
        if a=="H":
            points+=8
        if a=="I":
            points+=9
        if a=="J":
            points+=10
        if a=="K":
            points+=11
        if a=="L":
            points+=12
        if a=="M":
            points+=13
        if a=="N":
            points+=14
        if a=="O":
            points+=15
        if a=="P":
            points+=16
        if a=="Q":
            points+=17
        if a=="R":
            points+=18
        if a=="S":
            points+=19
        if a=="T":
            points+=20
        if a=="U":
            points+=21
        if a=="V":
            points+=22
        if a=="W":
            points+=23
        if a=="X":
            points+=24
        if a=="Y":
            points+=25
        if a=="Z":
            points+=26
    return points

lines = open("euler22file", 'r').readlines()
wherearrive=0
totalpoints=0
for mot in lines:
    wherearrive+=1
    points=countpoints(mot)
    totalpoints+=wherearrive*points
print totalpoints




