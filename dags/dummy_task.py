
def dummyVal():
    l = []
    c = 0
    while True:
        c +=1
        l.append(c)

        if c >= 100:
            # break
            return sum(l)
            break