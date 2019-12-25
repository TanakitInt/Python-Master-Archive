"""week11_02.Float that is not float"""
def main():
    """start!"""
    number = input()
    number = number.split('.')
    #split number
    number_front = int(number[0])
    number_back = int(number[1])
    #number_front process
    number_front = number_front + 5
#-----------------unused code------------------#
#
#    #number_back for demical count process
#    number_back_list = [ ]
#    for i in number_back:
#        number_back_list.append(i)
#    count_number_back = len(number_back_list)
#
#----------------------------------------------#
    #number_back process
    #from the sample '99'.ljust(5,'0')                     (n,'0')
    #it will be filled up '0' for n digits as requested for ^
    number_back = str(number_back)
    if int(number_back) < 999999:
        number_back = number_back.ljust(6, '0')
    else:
        list_ = []
        if int(number_back[6]) >= 5:
            num0 = number_back[0]
            list_.append(num0)
            num1 = number_back[1]
            list_.append(num1)
            num2 = number_back[2]
            list_.append(num2)
            num3 = number_back[3]
            list_.append(num3)
            num4 = number_back[4]
            list_.append(num4)
            if int(number_back[5]) + 1 >= 10:
                list_.append('0')
            else:
                num5 = int(number_back[5]) + 1
                num5 = str(num5)
                list_.append(num5)
        else:
            num0 = number_back[0]
            list_.append(num0)
            num1 = number_back[1]
            list_.append(num1)
            num2 = number_back[2]
            list_.append(num2)
            num3 = number_back[3]
            list_.append(num3)
            num4 = number_back[4]
            list_.append(num4)
            num5 = number_back[5]
            list_.append(num5)
        #force a list to reformat to end = ""
        new = ''
        new = new.join(list_)
        number_back = new
    #print!
    print(str(number_front) + '.' + str(number_back))
main()
