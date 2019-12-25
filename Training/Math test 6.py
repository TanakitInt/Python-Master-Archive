"""Math test 6"""
def main():
    """Circle for all"""
    radius = int(input())
    import math
    circle_circumference = 2*math.pi*radius
    circle_area = math.pi*(radius**2)
    circle_volume = (4/3)*math.pi*(radius**3)
    print(int(circle_circumference), "cm")
    print(int(circle_area), "cm^2")
    print(int(circle_volume), "cm^3")
main()
