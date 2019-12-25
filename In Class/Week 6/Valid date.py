"""Valid date"""
def main():
    """Start!"""
    date = input()
    import calendar
 
    #start split a date string input
    [month, day, year] = date.split("/")
    #detect [month, day, year] error in this form : MM/DD/YYYY
    month = int(month)
    day = int(day)
    year = int(year)
    if int(year) <= 0:
        print('%.2d'%month + "/" + '%.2d'%day + "/" + '%.4d'%year, "is invalid.")
    elif int(month) > 12 or int(month) <= 0:
        print('%.2d'%month + "/" + '%.2d'%day + "/" + '%.4d'%year, "is invalid.")
    elif int(day) > 31 or int(day) <= 0:
        print('%.2d'%month + "/" + '%.2d'%day + "/" + '%.4d'%year, "is invalid.")
    elif int(day) <= 31 and int(day) > 0:
        if int(month) in [4, 6, 9, 11]:
            if int(day) == 31:
                print('%.2d'%month + "/" + '%.2d'%day + "/" + '%.4d'%year, "is invalid.")
            else:
                print('%.2d'%month + "/" + '%.2d'%day + "/" + '%.4d'%year, "is valid.")
        elif int(month) == 2:
            if calendar.isleap(int(year)) == False and int(day) == 29:
                print('%.2d'%month + "/" + '%.2d'%day + "/" + '%.4d'%year, "is invalid.")
            else:
                print('%.2d'%month + "/" + '%.2d'%day + "/" + '%.4d'%year, "is valid.")
        else:
            print('%.2d'%month + "/" + '%.2d'%day + "/" + '%.4d'%year, "is valid.")
    else:
        print('%.2d'%month + "/" + '%.2d'%day + "/" + '%.4d'%year, "is valid.")
main()
 
#workspace
#'%.2d%month + "/" + '%.2d'%day + "/" + '%.04d'%year