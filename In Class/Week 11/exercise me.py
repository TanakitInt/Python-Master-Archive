import math as m
def cal_area(radius):
    areas = m.pi*radius**2
    return areas

def cal_circumference(radius):
    circumferences = 2*m.pi*radius
    return circumferences

def main():
    input_str = input('Please insert sequence of radius, seperated by comma: ').split(',')
    # create list from input sequence
    radius = []
    for i in input_str:
        radius.append(float(i))
    # map cal_area with sequence of radius
    areas = list(map(cal_area, radius))
    # map cal_circumference with sequence of radius
    circumferences = list(map(cal_circumference, radius))

    for i in range(len(radius)):
        print('radius: {0:.2f}, area: {1:.2f}, circumference: {2:.2f}'.format(radius[i], areas[i], circumferences[i]))

if __name__ == '__main__':
    main()
