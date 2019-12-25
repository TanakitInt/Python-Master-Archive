"""Palindrome"""
def main():
    """start"""
    text = str(input())

    text_invert = list(text)
    text_invert = text_invert[::-1]

    new = ''
    new = new.join(text_invert)

    text_invert = new

    if text == text_invert:
        print(text, "is Palindrome.")
    else:
        print("This is not Palindrome")
main()
