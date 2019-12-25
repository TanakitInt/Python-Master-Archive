"""Swap Word"""
def main():
    """start"""
    text = input()
    list_text = list(text)
    new_list = []

    for i in list_text:
        if i.isupper() == True:
            i = i.lower()
            new_list.append(i)
        elif i.islower() == True:
            i = i.upper()
            new_list.append(i)
        else:
            new_list.append(i)

    new = ''
    new = new.join(new_list)

    print(new)

    #swap case in 1 line.
    #text = input()
    #print(text.swapcase())

main()
