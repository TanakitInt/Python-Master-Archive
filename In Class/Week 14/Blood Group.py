"""Blood Group"""
def main():
    """start"""
    number = int(input())
    box = []

    while number > 0:
        input_ = input()
        filtered_item = input_.split(",")
        blood_raw = filtered_item[1]
        box.append(blood_raw)

        number = number - 1

    first = box.count('A')
    secound = box.count('B')
    third = box.count('O')
    fourth = box.count('AB')

    print(first)
    print(secound)
    print(third)
    print(fourth)
main()

