def main1():
    for ch in 'aardvark':
        print(ch)
main1()

def main2():
    for w in 'Now is the winter of our discontent...'.split():
        print(w)
main2()

def main3():
    for w in 'Mississippi'.split('i'):
        print(w, end=' ')
main3()

def main4():
    msg = ''
    for s in 'secret'.split('e'):
        msg = msg + s
    print(msg)
main4()

def main5():
    msg = ''
    for ch in 'secret':
        msg = msg + chr(ord(ch+1))
    print(msg)
main5()
