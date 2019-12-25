"""
leap year?
"""
def main():
    """
    start!
    """
    year = int(input())

    import calendar

    if calendar.isleap(year):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")
main()
