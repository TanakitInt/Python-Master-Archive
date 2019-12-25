# month.py
# Print the abbreviation of a month, given its number

def main():
    # months is used as a lookup table
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    # get user input
    nth_month = eval(input("Enter a month number (1-12): "))
    # compute starting position of month nth in months
    index = (nth_month-1) * 3    
    # Grab the appropriate slice from months
    monthAbbrev = months[index:index+3]
    # print the result    
    print("The month abbreviation is", monthAbbrev + ".")

main()
