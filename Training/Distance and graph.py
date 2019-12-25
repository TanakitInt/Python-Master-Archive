"""Sample graph (X,Y)"""
def graph():
    """Start"""
    point_1_x = float(input())
    point_1_y = float(input())
    point_2_x = float(input())
    point_2_y = float(input())
    compute_x = (point_1_x-point_2_x)**2
    compute_y = (point_1_y-point_2_y)**2
    distance = compute_x+compute_y
    import math
    sqrt_distance = math.sqrt(distance)
    num1 = int(sqrt_distance)
    print("Distance =", num1)
graph()
