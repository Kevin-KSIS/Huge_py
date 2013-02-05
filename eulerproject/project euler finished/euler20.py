Array=[]
with open("euler20file") as f:
  while True:
    c = f.read(1)
    if not c:
      print "End of file"
      break
    Array+=c

realsmall=0
print Array
for a in Array:
    if a!='\n':
        realsmall+=int(a)
print realsmall
