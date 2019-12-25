"""Reverse list"""
def main():
    """start!"""
    request_rept = int(input())
    l1st = []
    while request_rept > 0:
        text = input()
        l1st.append(text)
        request_rept = request_rept - 1
    l1st.reverse()
    for i in l1st:
        print(i)
main()
