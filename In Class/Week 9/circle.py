#input radius and compute

import math as m

def cal_area(radius):
    radius = m.pi*(radius**2)
    return radius

def cal_circumference(radius):
    radius = 2*m.pi*radius
    return radius

def main():
    radius = float(input())
    print('%0.2f'%cal_area(radius))
    print('%0.2f'%cal_circumference(radius))
main()
