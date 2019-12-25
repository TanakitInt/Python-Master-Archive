"""Area"""
def area():
    """Compute"""
    width = int(input())
    height = int(input())
    triangle = int((1/2)*width*height)
    rectangle = int(width*height)
    print("Triangle Area :", triangle, "unit")
    print("Rectangle Area :", rectangle, "unit")
area()
