x = open(raw_input("File: ")).readlines()
listx = []
for a in x:
    if not a in listx:
        listx.append(a)
        open("ProxyWorking&Filtered", 'a').write(a)
