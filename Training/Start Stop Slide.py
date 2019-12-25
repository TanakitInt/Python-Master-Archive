"""I/O"""
def Rev():
    text = input("Please enter your text : ")
    start = int(input("Please enter your start : "))
    stop = int(input("Please enter your stop : "))
    slide = int(input("Please enter your slide : "))
    print (text[start:stop:slide])
Rev()
