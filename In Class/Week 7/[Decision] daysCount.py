"""[Decision] daysCount"""
def compute():
    """for compute module"""
    import calendar as cl
    str_date_in = str(input())
    #start process with string
    list_date = str_date_in.split("/")
    #location 0 is month, location 1 is day,
    #location 2 is year
    #------------some varible assignment-------------#
    day = list_date[1]
    day = int(day)
    year = list_date[2]
    year = int(year)
    month = list_date[0]
    month = int(month)
    day_total = 0
    day_special = 0
    day_total_complete = 0
    #-----------exception for invalid day------------#

    if day <= 0 or day >= 32 or month <= 0 or month >= 13 or year <= 0:
        print(str('%0.02d'%month)+"/"+str('%0.02d'%day)\
            +"/"+str('%0.04d'%year)+" is invalid")
        return 0
    else:
        pass
    #--------------------month-----------------------#
    if month in [1]: #Jan
        day_total = 0
    elif month in [2]: #Feb
        #check if leap year
        if cl.isleap(year) == True:
            day_special = 1
            if day >= 30 or day <= 0:
                print(str('%0.02d'%month)+"/"+str('%0.02d'%day)\
                    +"/"+str('%0.04d'%year)+" is invalid")
                return 0
            else:
                pass
        else:
            day_special = 0
            if day >= 29 or day <= 0:
                print(str('%0.02d'%month)+"/"+str('%0.02d'%day)\
                    +"/"+str('%0.04d'%year)+" is invalid")
                return 0
            else:
                pass
        day_total = 31
    elif month in [3]: #Mar
        day_total = 31 + 28
    elif month in [4]: #Apr
        day_total = 31 + 28 + 31
    elif month in [5]: #May
        day_total = 31 + 28 + 31 + 30
    elif month in [6]: #Jun
        day_total = 31 + 28 + 31 + 30 + 31
    elif month in [7]: #Jul
        day_total = 31 + 28 + 31 + 30 + 31 + 30
    elif month in [8]: #Aug
        day_total = 31 + 28 + 31 + 30 + 31 + 30 + 31
    elif month in [9]: #Sep
        day_total = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31
    elif month in [10]: #Oct
        day_total = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30
    elif month in [11]: #Nov
        day_total = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31
    elif month in [12]: #Dec
        day_total = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30
    day_total_complete = day + day_special + day_total
    #-----------first, second and third day will be excepted----------#
    if day_total_complete%10 == 1:
        print(str('%0.02d'%month)+"/"+str('%0.02d'%day)+"/"+str('%0.04d'%year)\
            +" is the "+str(day_total_complete)+"st days of the year")
    elif day_total_complete%10 == 2:
        print(str('%0.02d'%month)+"/"+str('%0.02d'%day)+"/"+str('%0.04d'%year)\
            +" is the "+str(day_total_complete)+"nd days of the year")
    elif day_total_complete%10 == 3:
        print(str('%0.02d'%month)+"/"+str('%0.02d'%day)+"/"+str('%0.04d'%year)\
            +" is the "+str(day_total_complete)+"rd days of the year")
    else:
        print(str('%0.02d'%month)+"/"+str('%0.02d'%day)+"/"+str('%0.04d'%year)\
            +" is the "+str(day_total_complete)+"th days of the year")
compute()
