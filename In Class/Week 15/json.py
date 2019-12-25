"""json"""
def main():
    """json is just a string to list"""
    list_in = input()

    count = 0
    long_ = len(list_in)
    new_list = []


    for i in list_in:
        if i.isdigit() == True:
            i = int(i)
            count = count + 1
            if i%2 == 0:
                new_list.append(i)

        else:
            count = count + 1
            if count > long_:
                break

    for i in new_list:
        print(i)

main()
