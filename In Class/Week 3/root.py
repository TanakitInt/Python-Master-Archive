#distance between two dots

#start Eiei

def main():
    x1 = float(input("PLease enter your x1 value : "))
    y1 = float(input("PLease enter your y1 value : "))
    x2 = float(input("PLease enter your x2 value : "))
    y2 = float(input("PLease enter your y2 value : "))

    #start calculation Eiei

    import math
    compute_x = x2-x1
    compute_y = y2-y1
    addiction_result = compute_x**2 + compute_y**2
    root = math.sqrt(addiction_result)

    #output
    out = "Your result is : ", root
    print(out)

main()
