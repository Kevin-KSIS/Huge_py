points=0
def letterone(letter):
    global points
    if letter=='1':
        points+=3
        return points
    elif letter=='2':
        points+=3
        return points
    elif letter=='3':
        points+=5
        return points
    elif letter=='4':
        points+=4
        return points
    elif letter=='5':
        points+=4
        return points
    elif letter=='6':
        points+=3
        return points
    elif letter=='7':
        points+=5
        return points
    elif letter=='8':
        points+=5
        return points
    elif letter=='9':
        points+=4
        return points
def lettertwo(letter):
    global points
    if letter[0]=='0':
        letterone(letter[1:])
    #######################from 10 to 19###############
    if letter[0]=='1':
        if letter[1]=='0':
            points+=3
            return points
        if letter[1]=='1':
            points+=6 #eleven
            return points
        elif letter[1]=='2':
            points+=6 #twelve
            return points
        elif letter[1]=='3':
            points+=8 #thirteen
            return points
        elif letter[1]=='4':
            points+=8 #fourteen
            return points
        elif letter[1]=='5':
            points+=7   #fifteen
            return points
        elif letter[1]=='6':
            points+=7 #sixteen
            return points
        elif letter[1]=='7':
            points+=9 #seventeen
            return points
        elif letter[1]=='8':
            points+=9 #eightteen
            return points
        elif letter[1]=='9':
            points+=8 #nineteen
            return points
    ##############################others #########
    if letter[0]=='2':
        points+=6 #twenty
        if letter[1]!='0':
            points += letterone(letter[1])
            return points
        else:
            return points
    if letter[0]=='3':
        points+=6 #thirty
        if letter[1]!='0':
            points += letterone(letter[1])
            return points
        else:
            return points
    if letter[0]=='4':
        points+=6 #fourty
        if letter[1]!='0':
            points += letterone(letter[1])
            return points
        else:
            return points
    if letter[0]=='5':
        points+=5 #fifty
        if letter[1]!='0':
            points += letterone(letter[1])
            return points
        else:
            return points
    if letter[0]=='6':
        points+=5 #sixty
        if letter[1]!='0':
            points += letterone(letter[1])
            return points
        else:
            return points
    if letter[0]=='7':
        points+=7 #seventy
        if letter[1]!='0':
            points += letterone(letter[1])
            return points
        else:
            return points
    if letter[0]=='8':
        points+=6 #eighty
        if letter[1]!='0':
            points += letterone(letter[1])
            return points
        else:
            return points
    if letter[0]=='9':
        points+=6 #ninety nine
        if letter[1]!='0':
            points += letterone(letter[1])
            return points
        else:
            return points


########################################
def pointz(n):
    letter=str(n)
    if len(letter)==1:
        points = letterone(letter)
    elif len(letter)==2:
        points = lettertwo(letter)
    elif len(letter)==3:
        points=0
        if letter[0]=='1':
            points+=13    #one hundred and
            points += lettertwo(letter[1:])
            return points
        elif letter[0]=='2':
            points+=13
            points += lettertwo(letter[1:])
            return points
        elif letter[0]=='3':
            points+=15 #three
            points += lettertwo(letter[1:])
            return points
        elif letter[0]=='4':
            points+=14 #hundred and
            points += lettertwo(letter[1:])
            return points
        elif letter[0]=='5':
            points+=14
            points += lettertwo(letter[1:])
            return points
        elif letter[0]=='6':
            points+=13
            points += lettertwo(letter[1:])
            return points
        elif letter[0]=='7':
            points+=15
            points += lettertwo(letter[1:])
            return points
        elif letter[0]=='8':
            points+=15
            points += lettertwo(letter[1:])
            return points
        elif letter[0]=='9':
            points+=14
            points += lettertwo(letter[1:])
            return points
    elif len(letter)==4:
        return 8 #thousand
    return points


total=0
n=input("Enter a number (<1000) and it will calculates the total number of letter to arrive to this num:\n=> ")
for a in range(1,n+1):
    points=0
    number=pointz(a)
    print total
    total+=number
print total
