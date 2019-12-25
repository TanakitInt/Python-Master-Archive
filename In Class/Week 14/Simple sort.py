"""Simple sort"""
def main():
    """lelelel"""
    str_in = str(input())
    str_in = str_in.split(" ")

    temp = []
    for i in str_in:
        i = float(i)
        temp.append(i)

    temp = sorted(temp)

    temp2 = []
    for j in temp:
        j = '%0.3f'%j
        temp2.append(j)

    temp3 = []
    for k in temp2:
        k = str(k)
        temp3.append(k)

    for lel in temp3:
        print(lel, end=' ')

main()
