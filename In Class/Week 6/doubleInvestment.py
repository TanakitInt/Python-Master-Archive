"""doubleInvestment"""
def main():
    """start!"""
    interest = float(input())
    moneyin = 100
    year = 0
    while moneyin < 200:
        moneyin = moneyin * (interest + 1)
        year = year + 1
    print(year)
main()
