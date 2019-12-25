"""[Decision] easterPrediction"""
def main():
    """start"""
    import calendar as cl
    year_in = int(input())
    #exception for invalid year
    if year_in > 2099 or year_in < 1900:
        print("Invalid input.")
    else:
    #stop for exception
        a_num = year_in % 19
        b_num = year_in % 4
        c_num = year_in % 7
        d_num = ((19 * a_num) + 24) % 30
        e_num = ((2 * b_num) + (4 * c_num) + (6 * d_num) + 5) % 7
        march22_constant_notleap = 22
        #so february in leap year will be plus 1 -> (22+1)
        march22_constant_leap = 23
        if year_in in [1954, 1981, 2049, 2076]:
            if cl.isleap(year_in) == True:
                #minus 7 for delay
                day = march22_constant_leap + d_num + e_num - 31 - 7
            else:
                #minus 7 for delay
                day = march22_constant_notleap + d_num + e_num - 31 - 7
        else:
            if cl.isleap(year_in) == True:
                day = march22_constant_leap + d_num + e_num - 31
            else:
                day = march22_constant_notleap + d_num + e_num - 31
        #when easter day is not in April
        if day <= 0:
            if cl.isleap(year_in) == True:
                day = abs(day + 23 + 7)
                print("March "+str(day)+", "+str(year_in))
            else:
                day = abs(day + 22 + 7 + 2)
                print("March "+str(day)+", "+str(year_in))
        else:
            print("April "+str(day)+", "+str(year_in))
main()
