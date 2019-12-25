# month_list.py
# Print the abbreviation of a month, given its number using list

def main():
    # months is used as a lookup table
    months = ["Jan", "Feb", "Mar", "Apr", "May", 
          "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # get user input
    nth_month = eval(input("Enter a month number (1-12): "))
    # compute starting position of month nth in months
    index = (nth_month-1)    
    # Grab the appropriate slice from months
    monthAbbrev = months[index]
    # print the result    
    print("The month abbreviation is", monthAbbrev + ".")

main()
