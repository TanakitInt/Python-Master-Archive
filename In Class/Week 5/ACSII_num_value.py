"""ASCII to number"""
def main():
    """Start!"""
    string_input = str(input())
    splited = list(string_input)
    count = 0
    for i in splited:
        count = count + ord(i)
    print(count)
main()
