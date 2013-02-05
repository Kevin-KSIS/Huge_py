class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[1;32m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        CYAN = '\033[1;36m'
        COOL = '\033[0;45m'
        COOL1 = '\033[1;45m'

def allstrings(alphabet, length):
    """Find the list of all strings of 'alphabet' of length 'length'"""

    if length == 0: return []

    c = [[a] for a in alphabet[:]]
    if length == 1: return c

    c = [[x,y] for x in alphabet for y in alphabet]
    if length == 2: return c

    for l in range(2, length):
        c = [[x]+y for x in alphabet for y in c]

    return c

def toStringList(InputList):
    outputList = []
    for i in InputList:
        outputList.append(str(i))
    return outputList

def generate(size,appender, filex):
    for p in allstrings([0,1,2,3,4,5,6,7,8,9],size):
        open(filex,'a').write(appender+''.join(toStringList(p))+"\n")

size = input("\n"+ bcolors.COOL +"|---"+ bcolors.COOL1 +" Number List Generator"+ bcolors.COOL +" ---|"+ bcolors.ENDC +"\n\n["+ bcolors.CYAN +"*"+ bcolors.ENDC +"] Size of the list :\n"+bcolors.OKGREEN +"=>"+bcolors.ENDC +" ")
appender=raw_input("\n["+ bcolors.CYAN +"*"+ bcolors.ENDC +"] Enter the Number you want to append in front of the list :\n"+bcolors.OKGREEN +"=>"+bcolors.ENDC +" ")
filex=raw_input("\n["+ bcolors.CYAN +"*"+ bcolors.ENDC +"] Name the File you want to save to :\n"+bcolors.OKGREEN +"=>"+bcolors.ENDC +" ")
generate(size,appender,filex)




