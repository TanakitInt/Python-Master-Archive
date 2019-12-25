#calculate the volume and surface of circle

#start

def main():
    rad = float(input("Please enter your radius : "))
    print("This will calculate a volume and area of the circle")

    #calculate a volume
    import math
    vol = (4/3)*math.pi*(rad**3)

    #calulate an area
    area = 4*math.pi*(rad**2)

    print("Your volumn of the circle is :", vol)
    print("Your area of the circle is :", area)

#end
main()
