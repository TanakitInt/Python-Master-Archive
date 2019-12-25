# quadratic.py
#    A program that computes the real roots of a quadratic equation.
#    Illustrates use of the math library.
#    Note: this program crashes if the equation has no real roots.

def main():
    print("This program finds the real solutions to a quadratic\n")

    coeff_a = int(input("Please enter the coefficients a: "))
    coeff_b = int(input("Please enter the coefficients b: "))
    coeff_c = int(input("Please enter the coefficients c: "))
    
    # computing square root
    import math
    temp = math.sqrt(coeff_b * coeff_b - 4 * coeff_a * coeff_c)
    
    root1 = (-coeff_b + temp) / (2 * coeff_a) 
    root2 = (-coeff_b - temp) / (2 * coeff_a)
    
    print("The solutions are:", root1, root2 )

main()
