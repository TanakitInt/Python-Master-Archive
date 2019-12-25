"""Upper-Lower_case"""
def case_invert():
    """Begin"""
    text_input = str(input())
    text1 = str.upper(text_input)
    text2 = str.lower(text_input)
    text3 = str.swapcase(text_input)
    print(text1)
    print(text2)
    print(text3)
case_invert()
