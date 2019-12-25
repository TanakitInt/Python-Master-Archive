"""perfect number"""
def components():
    """find components of the number"""
    number = int(input())
    count = 1
    list_components = []
    while number > count:
        if number%count == 0:
            list_components.append(count)
        count = count + 1
    #compare an answer if supplyment of components are equal to number"""
    summation = sum(list_components)
    if summation != number:
        count = 0
        while len(list_components) > count+1:
            print(str(list_components[count])+" + ", end="")
            count = count + 1
        print(list_components[-1], end="")
        print(" = "+str(summation))
        print("Oops!!! This is not a perfect number.")
    else:
        count = 0
        while len(list_components) > count+1:
            print(str(list_components[count])+" + ", end="")
            count = count + 1
        print(list_components[-1], end="")
        print(" = "+str(number))
        print("Yes!!! This is a perfect number.")
components()
