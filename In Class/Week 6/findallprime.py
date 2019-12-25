"""Find all prime"""
def main():
    """This will find a prime number to n"""
    number = int(input())
    count = 2
    prime = []
    notprime = []
    while number > 0:
        while number > count:
            if number%count > 0:
                count = count + 1
            else:
                notprime.append(number)
                number = number - 1
                count = 2
        prime.append(number)
        number = number - 1
        count = 2
    #----------------remove 1 from list---------------#
    if 1 in prime:
        prime.remove(1)
    #-------------------print prime-------------------#
    prime.sort()
    for i in prime:
        print(i, end=" ")
main()
