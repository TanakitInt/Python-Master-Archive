#height of the ladder

#start

def main():
    height = float(input("Your height here : "))
    angle = float(input("Your angle here : "))

    import math
    rad = math.radians(angle)
    long_ladder = height/rad
    print("Result :", long_ladder)

#end
main()
