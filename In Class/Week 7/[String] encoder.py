"""[String] encoder"""
def main():
    """start!"""
    #--------------------Input--------------------#
    string_in = str(input())
    number = int(input())
    #---------------------------------------------#
    big_alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"*10**3
    small_alpha = "abcdefghijklmnopqrstuvwxyz"*10**3
    #---------------------------------------------#
    string_in = list(string_in)
    count = len(string_in)
    while count > 0:
        for i in string_in:
            location = big_alpha.find(i)
            print(small_alpha[location+number], end="")
            count = count - 1
main()
