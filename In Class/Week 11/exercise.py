import math
def cal_area(radius):
    # area = pi*radius*2
    return (0)

def cal_circumference(radius):
    # circumference = 2*pi*radius
    return (0)

def main():
    input_str = input('Please insert sequence of radius, seperated by comma: ').split(',')
    # create list from input sequence
    radius = []
    # map cal_area with sequence of radius
    areas = list(map())
    # map cal_circumference with sequence of radius
    circumferences = list(map())

    for i in range(len(radius)):
        print('radius: {0:.2f}, area: {1:.2f}, circumference: {2:.2f}'.format(radius[i], areas[i], circumferences[i]))

if __name__ == '__main__':
    main()
