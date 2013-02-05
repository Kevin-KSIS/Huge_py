for a1 in 'abcdefghijklmnopqrstuvwxyz':
    for a2 in 'abcdefghijklmnopqrstuvwxyz1234567890_-':
        pwd = a1+a2

        open('combinasions3letter', 'a').write(pwd+'\n\n')
