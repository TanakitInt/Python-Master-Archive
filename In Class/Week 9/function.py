def addInterest(balances, rate):

    empty = []
    for i in range(len(balances)):
        empty.append(balances[i] * (1 + rate))
    return empty

def main():
    amount = [10, 100 ,1000]
    rate = 0.05
    output = addInterest(amount, rate)
    print("Amount :", amount)
    print("Output :", output)
main()
