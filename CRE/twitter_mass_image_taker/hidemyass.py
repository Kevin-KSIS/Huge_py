import re,mechanize,threading,time
#generate a browser
def createbrowser():
    br = mechanize.Browser()
    br.set_handle_gzip(True)
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1 like Mac OS X; en-US) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9B179 Safari/7534.48.3')]
    return br

br = createbrowser()
for a in xrange(28):
    br.open("http://hidemyass.com/proxy-list/"+str(a))
    open("hidemyass.txt",'w').write(br.response().read())
    my_file = open("hidemyass.txt",'r').read()

    #remove what is display:none:
    for change in re.findall("display:none\">([0-9]*)",my_file) :
        my_file = my_file.replace("display:none\">"+change,"display:none\">")
    for change in re.findall("display:none\">([0-9]*)",my_file) :
        my_file = my_file.replace("display:none\">"+change,"display:none\">")
    for change in re.findall("display:none\">([0-9]*)",my_file) :
        my_file = my_file.replace("display:none\">"+change,"display:none\">")
    print re.findall("display:none\">([0-9]*)",my_file)

    #remove the class that does not display:
    searchforthose = re.findall(".(.*){display:none}",my_file)
    for sear in searchforthose:
        toremove = re.findall('<span class=\"'+sear+'\">([0-9]*)',my_file)
        for remov in toremove:
            if len(remov)==3:
                my_file = my_file.replace('<span class=\"'+sear+'\">'+remov,"<span class=\"\">")
        for remov in toremove:
            if len(remov)==2:
                my_file = my_file.replace('<span class=\"'+sear+'\">'+remov,"<span class=\"\">")
        for remov in toremove:
            if len(remov)==1:
                my_file = my_file.replace('<span class=\"'+sear+'\">'+remov,"<span class=\"\">")
    searchforthose = re.findall(".(.*){display:none}",my_file)
    print re.findall(".(.*){display:none}",my_file)


    #try to find ips BUT WHAT IF THE CLASS IS NUMBERS:
    numbers_class = re.findall("<span class=\"([0-9]*)\">",my_file)
    for number in numbers_class:
        my_file = my_file.replace('<span class=\"'+number,'<span class=\"')
    numbers_class = re.findall("<span class=\"([0-9]*)\">",my_file)
    for number in numbers_class:
        my_file = my_file.replace('<span class=\"'+number,'<span class=\"')
    numbers_class = re.findall("<span class=\"([0-9]*)\">",my_file)
    for number in numbers_class:
        my_file = my_file.replace('<span class=\"'+number,'<span class=\"')

    print re.findall("<span class=\"([0-9]*)\">",my_file)


    my_file = my_file.replace(".","")
    my_file = my_file.replace("socks4/5","")
    my_file = my_file.replace("page10","")
    my_file = my_file.replace("page25","")
    my_file = my_file.replace("page50","")
    my_file = my_file.replace("page100","")
    my_file = my_file.replace("per 0","")
    my_file = my_file.replace("2012<","<")
    my_file = my_file.replace('class="inactivepagination">1</li><li><a href="/proxy-list/2">2</a></li><li><a href="/proxy-list/3">3</a></li><li><a href="/proxy-list/4">4</a></li><li><a href="/proxy-list/5">5</a></li><li><a href="/proxy-list/6">6</a></li><li><a href="/proxy-list/7">7</a></li><li><a href="/proxy-list/8">8</a></li><li><a href="/proxy-list/9">9</a></li><li><a href="/proxy-list/10">10</a></li><li><a href="/proxy-list/11">11</a></li><li><a href="/proxy-list/12">12</a></li><li><a href="/proxy-list/13">13</a></li><li><a href="/proxy-list/14">14</a></li><li><a href="/proxy-list/15">15</a></li><li><a href="/proxy-list/16">16</a></li><li><a href="/proxy-list/17">17</a></li><li></li><li><a href="/proxy-list/27">27</a></li><li><a href="/proxy-list/28">28</a></li><li class="nextpageactive"><a href="/proxy-list/2" class="next">Next &#187;</a></li></div>','')
    my_file = my_file.replace('<a href="/proxy-list/1" class="prev">&#171; Previous</a></li><li><a href="/proxy-list/1">1</a></li><li class="inactivepagination">2</li><li><a href="/proxy-list/3">3</a></li><li><a href="/proxy-list/4">4</a></li><li><a href="/proxy-list/5">5</a></li><li><a href="/proxy-list/6">6</a></li><li><a href="/proxy-list/7">7</a></li><li><a href="/proxy-list/8">8</a></li><li><a href="/proxy-list/9">9</a></li><li><a href="/proxy-list/10">10</a></li><li><a href="/proxy-list/11">11</a></li><li><a href="/proxy-list/12">12</a></li><li><a href="/proxy-list/13">13</a></li><li><a href="/proxy-list/14">14</a></li><li><a href="/proxy-list/15">15</a></li><li><a href="/proxy-list/16">16</a></li><li><a href="/proxy-list/17">17</a></li><li></li><li><a href="/proxy-list/27">27</a></li><li><a href="/proxy-list/28">28</a>','')
    my_file = my_file.replace('a href="/proxy-list/2" class="prev">&#171; Previous</a></li><li><a href="/proxy-list/1">1</a></li><li><a href="/proxy-list/2">2</a></li><li class="inactivepagination">3</li><li><a href="/proxy-list/4">4</a></li><li><a href="/proxy-list/5">5</a></li><li><a href="/proxy-list/6">6</a></li><li><a href="/proxy-list/7">7</a></li><li><a href="/proxy-list/8">8</a></li><li><a href="/proxy-list/9">9</a></li><li><a href="/proxy-list/10">10</a></li><li><a href="/proxy-list/11">11</a></li><li><a href="/proxy-list/12">12</a></li><li><a href="/proxy-list/13">13</a></li><li><a href="/proxy-list/14">14</a></li><li><a href="/proxy-list/15">15</a></li><li><a href="/proxy-list/16">16</a></li><li><a href="/proxy-list/17">17</a></li><li></li><li><a href="/proxy-list/27">27</a></li><li><a href="/proxy-list/28">28</a></li><li class="nextpageactive"><a href="/proxy-list/4" cla','')
    my_file = my_file.replace('a href="/proxy-list/3" class="prev">&#171; Previous</a></li><li><a href="/proxy-list/1">1</a></li><li><a href="/proxy-list/2">2</a></li><li><a href="/proxy-list/3">3</a></li><li class="inactivepagination">4</li><li><a href="/proxy-list/5">5</a></li><li><a href="/proxy-list/6">6</a></li><li><a href="/proxy-list/7">7</a></li><li><a href="/proxy-list/8">8</a></li><li><a href="/proxy-list/9">9</a></li><li><a href="/proxy-list/10">10</a></li><li><a href="/proxy-list/11">11</a></li><li><a href="/proxy-list/12">12</a></li><li><a href="/proxy-list/13">13</a></li><li><a href="/proxy-list/14">14</a></li><li><a href="/proxy-list/15">15</a></li><li><a href="/proxy-list/16">16</a></li><li><a href="/proxy-list/17">17</a></li><li></li><li><a href="/proxy-list/27">27</a></li><li><a href="/proxy-list/28">28</a></li><li class="nextpageactive"><a href="/proxy-list/5" class=','')
    my_file = my_file.replace('a href="/proxy-list/4" class="prev">&#171; Previous</a></li><li><a href="/proxy-list/1">1</a></li><li><a href="/proxy-list/2">2</a></li><li><a href="/proxy-list/3">3</a></li><li><a href="/proxy-list/4">4</a></li><li class="inactivepagination">5</li><li><a href="/proxy-list/6">6</a></li><li><a href="/proxy-list/7">7</a></li><li><a href="/proxy-list/8">8</a></li><li><a href="/proxy-list/9">9</a></li><li><a href="/proxy-list/10">10</a></li><li><a href="/proxy-list/11">11</a></li><li><a href="/proxy-list/12">12</a></li><li><a href="/proxy-list/13">13</a></li><li><a href="/proxy-list/14">14</a></li><li><a href="/proxy-list/15">15</a></li><li><a href="/proxy-list/16">16</a></li><li><a href="/proxy-list/17">17</a></li><li></li><li><a href="/proxy-list/27">27</a></li><li><a href="/proxy-list/28">28</a></li><li class="nextpageactive"><a href="/proxy-list/6" cl','')
    my_file = my_file.replace('a href="/proxy-list/4" class="prev">&#171; Previous</a></li><li><a href="/proxy-list/1">1</a></li><li><a href="/proxy-list/2">2</a></li><li><a href="/proxy-list/3">3</a></li><li><a href="/proxy-list/4">4</a></li><li class="inactivepagination">5</li><li><a href="/proxy-list/6">6</a></li><li><a href="/proxy-list/7">7</a></li><li><a href="/proxy-list/8">8</a></li><li><a href="/proxy-list/9">9</a></li><li><a href="/proxy-list/10">10</a></li><li><a href="/proxy-list/11">11</a></li><li><a href="/proxy-list/12">12</a></li><li><a href="/proxy-list/13">13</a></li><li><a href="/proxy-list/14">14</a></li><li><a href="/proxy-list/15">15</a></li><li><a href="/proxy-list/16">16</a></li><li><a href="/proxy-list/17">17</a></li><li></li><li><a href="/proxy-list/27">27</a></li><li><a href="/proxy-list/28">28</a></li><li class="nextpageactive"><a href="/proxy-list/6" class=','')
    my_file = my_file.replace('a href="/proxy-list/5" class="prev">&#171; Previous</a></li><li><a href="/proxy-list/1">1</a></li><li><a href="/proxy-list/2">2</a></li><li><a href="/proxy-list/3">3</a></li><li><a href="/proxy-list/4">4</a></li><li><a href="/proxy-list/5">5</a></li><li class="inactivepagination">6</li><li><a href="/proxy-list/7">7</a></li><li><a href="/proxy-list/8">8</a></li><li><a href="/proxy-list/9">9</a></li><li><a href="/proxy-list/10">10</a></li><li><a href="/proxy-list/11">11</a></li><li><a href="/proxy-list/12">12</a></li><li><a href="/proxy-list/13">13</a></li><li><a href="/proxy-list/14">14</a></li><li><a href="/proxy-list/15">15</a></li><li><a href="/proxy-list/16">16</a></li><li><a href="/proxy-list/17">17</a></li><li></li><li><a href="/proxy-list/27">27</a></li><li><a href="/proxy-list/28">28</a></li><li class="nextpageactive"><a href="/proxy-list/7','')

    time.sleep(5)

    open("thisisatest.txt",'w').write(my_file)

    iterator = 0
    newip = ""
    THEips = re.findall("([0-9]+)<",my_file)

    THEips = re.findall("([0-9]+)<",my_file)
    for ip in THEips:
        if iterator==3:
            newip += ip+":"
        elif iterator == 4:
            newip+=ip
        else:
            newip += ip+"."
        iterator += 1

        if iterator == 5:
            if newip not in open("hidemyassips.txt",'r').read():
                open("hidemyassips.txt",'a').write(newip+"\n")
                print newip+"\n"

            iterator = 0
            newip=""
    if a==6:
        exit(0)
