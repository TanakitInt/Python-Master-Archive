"""Hit the circle"""
def circle():
    """Lowest point of spere"""
    x = int(input())
    y = int(input())
    z = int(input())
    r = int(input())
    y_low_by_r = (y-r)
    circle_center_low_by_r = (x, y-r, z)
    print(circle_center_low_by_r)
circle()
