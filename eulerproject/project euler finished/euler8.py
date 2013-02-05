Array=[]
with open("euler8file") as f:
  while True:
    c = f.read(1)
    if not c:
      print "End of file"
      break
    Array+=c

realsmall=0
print Array
for a in range(0,996):
    if Array[a]!='\n' and Array[a+1]!='\n' and Array[a+2]!='\n' and Array[a+3]!='\n' and Array[a+4]!='\n':
        if int(Array[a])*int(Array[a+1])*int(Array[a+2])*int(Array[a+3])*int(Array[a+4])>realsmall:
            realsmall=int(Array[a])*int(Array[a+1])*int(Array[a+2])*int(Array[a+3])*int(Array[a+4])
print realsmall

