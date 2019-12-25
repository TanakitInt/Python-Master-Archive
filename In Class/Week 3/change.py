# change.py
# A program to calculate the value of some change in Thai baht

def main():  
    print("Change Counter\n") 
    print("Please enter the count of each coin type:")    
    baht_10 = int(input("10 baht coins: "))
    baht_05 = int(input("5 baht coins: "))
    baht_02 = int(input("2 baht coins: "))
    baht_01 = int(input("1 baht coins: "))
    satang_50 = int(input("50 satang coins: "))
    satang_25 = int(input("25 satang coins: "))
    
    # compute the total value of change
    total = (baht_10*10)+(baht_05*5)+(baht_02*2)+(baht_01*1)\
    +(satang_50*0.5)+(satang_25*0.25)
    
    print("The total value of your change is ", total, " baht")

main()
