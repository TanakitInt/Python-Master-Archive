"""Math test 4"""
def math():
    """Compute!"""
    base = int(input())
    indicator = int(input())
    first_compute = (base**indicator)
    second_compute = (base+indicator)
    third_compute = (first_compute+second_compute)
    print(third_compute)
math()
