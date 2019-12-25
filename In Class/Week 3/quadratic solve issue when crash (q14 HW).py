#--------------------------Information------------------------------#
#Tanakit Intaniyom DSBA

#Assignment Week 3
#Question number 14
#Last updated on 26/08/2017 at 02.44 am
#-------------------------------------------------------------------#
# quadratic.py
#    A program that computes the real roots of a quadratic equation.
#    Illustrates use of the math library.
#    Note: this program crashes if the equation has no real roots.

#def main():
    #print("This program finds the real solutions to a quadratic\n")

    #coeff_a = int(input("Please enter the coefficients a: "))
    #coeff_b = int(input("Please enter the coefficients b: "))
    #coeff_c = int(input("Please enter the coefficients c: "))
    
    # computing square root
    #temp = square_root(coeff_b * coeff_b - 4 * coeff_a * coeff_c)
    
    #root1 = (-coeff_b + temp) / (2 * coeff_a)
    #root2 = (-coeff_b - temp) / (2 * coeff_a)
    
    #print("The solutions are:", root1, root2 )

#main()

#-------------------The upper is original code----------------------#
#start fixing an error
#   the error will cause when x == (-b +-(sqrt(b**2-4*a*c))/2*a is
#not in real number path

def main():
    num_a = int(input("Please enter the coefficients a: "))
    num_b = int(input("Please enter the coefficients b: "))
    num_c = int(input("Please enter the coefficients c: "))

    #start computation
    #A +- symbol is currently not found in python module by me
    #then split it into two equation

    import math

    #insert a condition that inside a square root must not less than 0 and
    #2*a is not equal 0 too. There would be an error occured.

    if num_b**2-4*num_a*num_c >= 0 and 2*num_a != 0:
        #for plus
        x_plus = (-num_b+(math.sqrt(num_b**2-4*num_a*num_c)))/2*num_a

        #for minus
        x_minus = (-num_b-(math.sqrt(num_b**2-4*num_a*num_c)))/2*num_a

        #start printing an answer of x if x is real number path
        print("Your answer for x is : ", x_plus, x_minus)
    else:
        #start printing an error of x if x is not real number path
        print("Ummm... that was maybe an imaginary path \
answer or invalid square root or invalid input for a or b or c")
main()
#finish fixing an error
