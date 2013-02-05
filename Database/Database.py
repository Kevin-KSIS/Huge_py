import sqlite3, msvcrt, sys

def newgetpass(quest):
    password = ''
    print quest,
    while 1:
        passChar = msvcrt.getch()
        if passChar == chr(13):
            break
        elif passChar == '\b':
            try:
                password = password[:-1]
                os.system("cls")
                sys.stdout.write("Password: "+len(password)*"*")
            except:
                pass
        elif c == '\003':
            raise KeyboardInterrupt
        else:
            password += passChar
            sys.stdout.write("*")
    return password
conn = sqlite3.connect('MyDb.db')
c = conn.cursor()
try:
    c.execute('''create table users
(username text, pwd text)''')
except:
    pass
while 1:
    cond = input("""\t\t\t1.Add a user
\t\t\t2.Read content
\t\t\t3.Update user's password
\t\t\t4.Export Data
\t\t\t5.Delete user
\t\t\t6.Import a list of usernames and passwords
\t\t\t7.Delete Everything

What do you want to do: """)
    if cond == 1:
        try:
            user = raw_input("Account name: ")
            pasw = newgetpass("Password: ")
            c.execute("""insert into users
              values ('"""+ user+ """','""" + pasw + """')""")
            conn.commit()
            print
            print
        except:
            print "An error occured."
            print
            print

    elif cond == 2:
        try:
            x = c.execute('''SELECT * FROM users''')
            s = list(x)
            if len(s) > 0:
                for a in s:
                    print "User: " + a[0]
                    print "Pass: " + a[1]
            else:
                print ""
        except:
            print "An error has occured."

    elif cond ==3:
        try:
            usersid = raw_input("Username: ")
            newpwd = newgetpass("New password: ")
            c.execute("UPDATE users SET pwd=? WHERE username=?", (newpwd, usersid))
            conn.commit()
            print
            print
        except:
            print "An error occured."
            print
            print


    elif cond == 4:
        try:
            filex = open(raw_input("File Location: "), 'a')
            x = c.execute('''SELECT * FROM users''')
            for a in x:
                filex.write("User: " + a[0] + "\n")
                filex.write("Pass: " + a[1] + "\n")
                filex.write('\n\n')
            filex.close()
            print
            print
        except:
            print "An error Occured."
            print
            print

    elif cond == 5:
        try:
            usertodelete = raw_input("User: ")
            c.execute("DELETE FROM users WHERE username='" + usertodelete + "'")
            conn.commit()
            print
            print
        except:
            print "An error occured."
            print
            print

    elif cond == 6:
        try:
            fileread= open(raw_input("File: ")).readlines()
            for a in fileread:
                try:
                    a = a.rsplit()[0]
                    a = a.split(":")
                    c.execute("""insert into users
              values ('"""+ a[0]+ """','""" + a[1] + """')""")
                except:
                    pass
        except:
            print "An error occured opening the file."
            print
            print

        conn.commit()
        print
        print
    elif cond == 7:
        hey = raw_input("Are you sure? y/n: ")
        if hey == 'y':
            try:
                c.execute("DELETE FROM users")
                conn.commit()
            except:
                print "An error occured."
                print
                print
        else:
            pass




