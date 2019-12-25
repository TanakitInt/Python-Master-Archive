"""Whomost"""
def main():
    """start"""
    request_rept = int(input())
    l1st = []
    while request_rept > 0:
        text = input()
        l1st.append(text)
        l1st.sort()
        request_rept = request_rept - 1
    highscore = 0
    for i in l1st:
        point = l1st.count(i)
        if point > highscore:
            winner = i
            highscore = point
    print(winner)
    print(highscore)
main()
    