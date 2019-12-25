"""[Loop] scoreHistogram"""
def main():
    """Start!"""
    point_in = input()
    #empty list
    point_list = []
    list0 = []
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    #start split ","
    point_list = point_in.split(",")
    while len(point_list) > 0:
        point_count = point_list.sort()
        point_count = point_list.pop()
        point_count = float(point_count)
        if point_count >= 0 and point_count <= 1:
            list0.append(point_count)
        elif point_count > 1 and point_count <= 2:
            list1.append(point_count)
        elif point_count > 2 and point_count <= 3:
            list2.append(point_count)
        elif point_count > 3 and point_count <= 4:
            list3.append(point_count)
        elif point_count > 4 and point_count <= 5:
            list4.append(point_count)
        elif point_count > 5 and point_count <= 6:
            list5.append(point_count)
        elif point_count > 6 and point_count <= 7:
            list6.append(point_count)
        elif point_count > 7 and point_count <= 8:
            list7.append(point_count)
        elif point_count > 8 and point_count <= 9:
            list8.append(point_count)
        elif point_count > 9 and point_count <= 10:
            list9.append(point_count)
    print("0-1:"+"|"*len(list0))
    print("1-2:"+"|"*len(list1))
    print("2-3:"+"|"*len(list2))
    print("3-4:"+"|"*len(list3))
    print("4-5:"+"|"*len(list4))
    print("5-6:"+"|"*len(list5))
    print("6-7:"+"|"*len(list6))
    print("7-8:"+"|"*len(list7))
    print("8-9:"+"|"*len(list8))
    print("9-10:"+"|"*len(list9))
main()
