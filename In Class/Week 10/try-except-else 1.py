"""try-except-else 1"""
def test1():
    print('This is test1 function (with try-exception).')
    print('Test1: Section 1')
    try:
        x = eval(input('Please input X: '))
        y = eval(input('Please input Y: '))
        z = x+y
    except:
        #This will check for any exception
        #and print error when error
        print('Error!')
    else:
        print('Successfully completed the task.')
test1()

def test2():
    print('This is test1 function (with try-exception).')
    print('Test1: Section 1')
    try:
        x = eval(input('Please input X: '))
        y = eval(input('Please input Y: '))
        z = x+y
    except Exception as err:
        #Shorten an exception name
        #This will check for any exception
        #and print why it is error
        print('Exception: ', err)
    else:
        print('Successfully completed the task.')
test2()
