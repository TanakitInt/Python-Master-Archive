"""..."""
 
def main():
    """..."""
    date = input()
    date_saved = date
    #Get values
    month = int(date_saved[0:date_saved.index("/")])
    date_saved = date_saved[date_saved.index("/")+1:]
    day = int(date_saved[0:date_saved.index("/")])
    year = int(date_saved[date_saved.index("/")+1:])
 
    leap_year = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    month_30 = [4, 6, 9, 11]
    month_31 = [1, 3, 5, 7, 8, 10, 12]
 
    valid_0 = (month in month_30) and 0 < day <= 30 and 1 <= year <= 9999
    valid_1 = (month in month_31) and 0 < day <= 31 and 1 <= year <= 9999
    valid_2 = month == 2 and ((0 < day <= 28) or (leap_year and 0 < day <= 29))
 
    if valid_0 or valid_1:
        print("%02i/%02i/%04i is valid." %(month, day, year))
    elif valid_2:
        print("%02i/%02i/%04i is valid." %(month, day, year))
    else:
        print("%02i/%02i/%04i is invalid." %(month, day, year))
 
main()