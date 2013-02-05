import mechanize

def yahoochecker(email,fichier):
    domainlist=open("domainlist").readlines()
    for dico in domainlist:
        br = mechanize.Browser()
        br.set_handle_robots(False)
        br.set_handle_redirect(True)
        br.set_handle_gzip(True)
        br.addheaders = [('User-agent','Mozilla/5.0 (Windows; Windows NT 6.0; rv:11.0) Gecko/20100101 Firefox/11.0')]
        domain , domainend= dico.split(":")[0],dico.split(":")[1]
        lien = "https://edit.yahoo.com/reg_json?PartnerName=yahoo_default&AccountID="+email+"@"+domain+"&ApiName=ValidateFields&intl="+domainend
        br.open(str(lien))
        if "SUCCESS" in br.response().read():
            open(fichier, 'a').write(email+"@"+domain+"\n")
            print email+"@"+domain
        else:
          pass
        br.close()

email = raw_input("Enter the id you want to check:\n=> ")
fichier = raw_input("Enter where you want to save:\n=> ")
yahoochecker(email, fichier)
