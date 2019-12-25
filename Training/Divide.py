"""Division"""
def math():
    """This will divide an interger"""
    dividend = int(input())
    denominator = int(input())
    result_no_remain_state = dividend//denominator
    result_remain_interger = dividend%denominator
    print(result_no_remain_state+result_remain_interger)
math()
