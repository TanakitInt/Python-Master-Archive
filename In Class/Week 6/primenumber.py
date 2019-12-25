"""prime number"""
def main():
    """start!"""
    number = int(input())
    count = 2
    while number > count:
        if number%count > 0:
            count = count + 1
        else:
            print(number, "is not prime.")
            return 0
    print(number, "is prime.")
main()
