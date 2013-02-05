for a in range(100,1000):
    for b in range(100,1000):
        text=str(a*b)
        if len(text)%2==1:
            pass
        else:
            if text[0]==text[5] and text[1]==text[4] and text[2] == text[3]:
                print text
